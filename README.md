Galaxy Tool wrappers
====================

# Introduction

This repository is for the development of wrappers for tools of ASaiM Galaxy instance, *i.e* mainly metagenomic/metatranscriptomic tools. These wrappers are integrated in Galaxy ToolShed.

# Folder structure

Within the `tools` folder is one folder for each Tool released on the Galaxy Tool Shed. Each tools contains a `test-data` folder used for functional test sample data.

`packages` folder contains packages for Galaxy Tool Shed dependency definitions.

# Installation

The individual Galaxy tools, found in the `tools/` folder, must be installed into a Galaxy instance for use, generally via the Galaxy Tool Shed. 

# Testing

[![Build Status](https://travis-ci.org/ASaiM/galaxytools.svg)](https://travis-ci.org/ASaiM/galaxytools)

The tools are tested using [Travis CI](https://travis-ci.org/) after each update of this GitHub repository. These tests includes `planemo` tests (`lint`, `test`) to test dependencies installation and functional tests described `test` section of each wrapper.

See [`.travis.yml`](https://raw.githubusercontent.com/ASaiM/galaxytools/master/.travis.yml) file for more technical details.

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# License

ASaiM Galaxy tool wrappers are released under Apache 2 License. See the LICENSE file for details
