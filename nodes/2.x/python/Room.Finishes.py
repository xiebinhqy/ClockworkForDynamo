import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

items = UnwrapElement(IN[0])
version = IN[1]
if version > 2021: unittype = ForgeTypeId('autodesk.spec.aec:area-2.0.0')
else: unittype = UnitType.UT_Area

def InternalUnitToDisplayUnit(val, unittype):
	formatoptions = doc.GetUnits().GetFormatOptions(unittype)
	if version > 2021: dispunits = formatoptions.GetUnitTypeId()
	else: dispunits = formatoptions.DisplayUnits
	try: return UnitUtils.ConvertFromInternalUnits(val,dispunits)
	except: return None

def RoomFinishes(item):
	doc = item.Document
	calculator = SpatialElementGeometryCalculator(doc)
	options = Autodesk.Revit.DB.SpatialElementBoundaryOptions()
	# get boundary location from area computation settings
	boundloc = Autodesk.Revit.DB.AreaVolumeSettings.GetAreaVolumeSettings(doc).GetSpatialElementBoundaryLocation(SpatialElementType.Room)
	options.SpatialElementBoundaryLocation = boundloc
	mlist = []
	tlist = []
	elist = []
	alist = []
	flist = []
	try:
		results = calculator.CalculateSpatialElementGeometry(item)
		for face in results.GetGeometry().Faces:
			for bface in results.GetBoundaryFaceInfo(face):
				tlist.append(str(bface.SubfaceType))
				eId = bface.SpatialBoundaryElement.HostElementId
				if eId == ElementId.InvalidElementId:
					liId = bface.SpatialBoundaryElement.LinkInstanceId
					if liId == ElementId.InvalidElementId: 
						elist.append(None)
						mlist.append(None)
					else:
						leId = bface.SpatialBoundaryElement.LinkedElementId
						if leId == ElementId.InvalidElementId: 
							elist.append(None)
							mlist.append(None)
						else: 
							elist.append(doc.GetElement(liId).GetLinkDocument().GetElement(leId))
							if bface.GetBoundingElementFace().MaterialElementId.IntegerValue == -1: mlist.append(None)
							else: mlist.append(doc.GetElement(liId).GetLinkDocument().GetElement(bface.GetBoundingElementFace().MaterialElementId))
				else: 
					elist.append(doc.GetElement(eId))
					if bface.GetBoundingElementFace().MaterialElementId.IntegerValue == -1: mlist.append(None)
					else: mlist.append(doc.GetElement(bface.GetBoundingElementFace().MaterialElementId))
				alist.append(InternalUnitToDisplayUnit(bface.GetSubface().Area, unittype))
				flist.append(bface.GetBoundingElementFace())
		return tlist, mlist, alist, flist, elist
	except: return [],[],[],[],[]

if isinstance(IN[0], list): 
	results = [RoomFinishes(x) for x in items]
	OUT = list(zip(*results))
else: OUT = RoomFinishes(items)