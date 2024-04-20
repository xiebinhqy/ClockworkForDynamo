![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg) [![Current version](https://img.shields.io/github/v/release/andydandy74/ClockworkForDynamo?label=Current%20Version&color=brightgreen)](http://dynamopackages.com/) ![Node count](https://img.shields.io/github/directory-file-count/andydandy74/ClockworkForDynamo/nodes%2F2.x?type=file&label=Node%20Count&color=brightgreen) [![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-brightgreen.svg?style=flat)](https://github.com/andydandy74/ClockworkForDynamo/blob/master/.github/CONTRIBUTING.md) [![CodeQL](https://github.com/andydandy74/ClockworkForDynamo/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/andydandy74/ClockworkForDynamo/actions/workflows/github-code-scanning/codeql) [![Follow me on LinkedIn for updates](https://img.shields.io/badge/LinkedIn-0077B5?style=social&logo=linkedin)](https://www.linkedin.com/in/andreasdieckmann) 

![Clockwork logo](clockwork-logo.png)

**Clockwork** is a collection of custom nodes for the [Dynamo](http://www.dynamobim.com) visual programming environment. It contains many Revit-related nodes, but also lots of nodes for various other purposes such as list management, mathematical operations, string operations, geometric operations (mainly bounding boxes, meshes, planes, points, surfaces, UVs and vectors) and paneling. Currently it consists of some 450+ nodes of which a large portion was originally published in a number of separate packages.

Clockwork for Dynamo 2.x is currently developed in Dynamo 2.6.0 but also tested in newer 2.x versions which means it's compatible with Revit 2021 and later (and probably still working in Revit 2017-2020 as well).

## Installation
Installation is simple - just use Dynamo's built-in package manager and search for ```Clockwork```. Make sure you have the correct version of Clockwork installed that corresponds to your installed version of Dynamo (most likely 2.x). 
As of **Revit 2023** you will need to install the package **"DynamoIronPython2.7"** (also from the package manager). Dynamo's workspace reference view extension will prompt you to install version 2.1 of that package. **Don't do that!** Instead **install the latest version** of that package.

## Versions
The different versions are available as separate packages on the package manager. (So far each new major Dynamo version has introduced changes that prevented downward - and sometimes even upward - compatibility of nodes, hence the separate packages...)

Package name | Supported | Last version | Revit versions | Change log | Docs | Repository | Deprecated nodes | Samples
-- | -- | -- | -- | -- | -- | -- | -- | --
Clockwork for Dynamo **2.x** | :white_check_mark: | 2.6.0 | 2017-24 | [Changes](https://github.com/andydandy74/ClockworkForDynamo/wiki/Version-History) | [Docs](https://github.com/andydandy74/ClockworkForDynamo/wiki/2.x-Node-Documentation) | [Repo](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/2.x) | [Deprecation](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-2x) | [Samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/2.x)
Clockwork for Dynamo **1.x** | :x: | 1.34.0 | 2015-19 | [Changes](https://github.com/andydandy74/ClockworkForDynamo/wiki/1.x-Version-History) | [Docs](https://github.com/andydandy74/ClockworkForDynamo/wiki/1.x-Node-Documentation) | [Repo](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/1.x) | [Deprecation](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-1x) | [Samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/1.x)
Clockwork for Dynamo **0.9.x** | :x: | 0.90.8 | 2015-17 | [Changes](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.9.x-Version-History) | [Docs](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.9.x-Node-Documentation) | [Repo](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.9.x) | [Deprecation](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-09x)
Clockwork for Dynamo **0.8.2** | :x: | 0.82.8 | 2014-16 | [Changes](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.8.x-Version-History) | [Docs](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.8.x-Node-Documentation) | [Repo](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.8.x) | [Deprecation](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-082)
Clockwork for Dynamo **0.7.x** | :x: | 0.75.47 | 2014-16 | [Changes](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.7.x-Version-History) | [Docs](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.7.x-Node-Documentation) | [Repo](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.7.x) | [Deprecation](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#clockwork-for-dynamo-07x) | [Samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/0.7.x)
Clockwork for Dynamo **0.6.3** | :x: | 0.63.3 | 2013-14 |   | [Docs](https://github.com/andydandy74/ClockworkForDynamo/wiki/0.6.3-Node-Documentation) | [Repo](https://github.com/andydandy74/ClockworkForDynamo/tree/master/nodes/0.6.3) | [Deprecation](https://github.com/andydandy74/ClockworkForDynamo/wiki/Deprecated-Nodes-&-Packages#pre-clockwork-packages) | [Samples](https://github.com/andydandy74/ClockworkForDynamo/tree/master/package_samples/0.6.3)

Note that Clockwork version numbering follows the Dynamo version the package is currently maintained for, e.g. Clockwork for Dynamo 2.x v**2.0**.XXX is maintained in Dynamo **2.0**.0 while Clockwork for Dynamo 2.x v**2.3**.XXX would be maintained in Dynamo **2.0.3** and Clockwork for Dynamo 2.x v**2.30**.XXX would be maintained in Dynamo **2.3.0**...

## Renamed, recategorized and deprecated nodes
During migration from one Dynamo version to the next, I regularly recategorize, relabel and rename a lot of nodes. These changes are documented in an [excel sheet](https://github.com/andydandy74/ClockworkForDynamo/raw/master/NodeList.xlsx) that contains a list of all nodes within the package.

## Material on this repository
This repository contains the following:
- Directory [maintenance](maintenance) contains scripts that I use to keep Clockwork in shape, e.g. for creating the node documentation on the wiki, extracting Python scripts from custom nodes etc.
- Directory [nodes](nodes) is the actual repository of the custom nodes that I use for versioning nodes in between publishing package updates to Dynamo's package manager - which means you will sometimes find nodes in here that haven't made it onto the package manager yet.
- Directory [package_samples](package_samples) contains simple examples for most of the nodes in Clockwork. I use them for occasional testing, but they should also help explain how to use each node. All samples are available for the current versions - sample support for older versions is patchy at best.
- Directory [workflow_samples](workflow_samples) contains some old sample workflows that I have published online somewhere before. I have also included some of the examples that I used to use for teaching Dynamo as well as some material presented at conferences. Almost all of these are available for Dynamo 0.7.x (as well as 0.6.3). They will not be updated to a current version.

## Sponsoring?
This is free software. I've created and maintained it on my spare time for a number of years now.
I don't do Patreon or GitHub Sponsors and I'm not planning to.
However, if you are using this software or have done so in the past and it has increased your productivity, please consider giving something back nonetheless. If you're smart enough to use Dynamo, you're most probably smart enough to know climate change is real, too. And I'd like to believe you're already doing something to battle it at this point. 

Do more.

[![Bad Monkeys logo](https://www.badmonkeys.net/wp-content/uploads/2016/12/BadMonkey_finalLogo-01.png)](http://www.badmonkeys.net/)
