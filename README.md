Galaxy Tool wrappers
====================

# Introduction

This repository is for the development of wrappers for tools of ASaiM Galaxy 
instance, *i.e* mainly metagenomic/metatranscriptomic tools. These wrappers are
integrated in the Galaxy ToolShed.

# Folder structure

Within the `tools` folder is one folder for each Tool released on the Galaxy Tool 
Shed. Each tools contains a `test-data` folder used for functional test sample data.

`packages` folder contains packages for Galaxy Tool Shed dependency definitions.

All folders and subfolder contain additional `README` files with information 
such as installation.

# Installation

The individual Galaxy tools, found in the `tools/` folder, must be installed 
into a Galaxy instance for use, generally via the Galaxy Tool Shed. 
However, manual installation is possible as described in the `README`
 file of each tool.

# Testing

All of these Galaxy tools include a <tests> section in the tool XML files, which 
defines at least one functional test (sample input files, parameters and the 
expected output). 

If the tools are installed, theses tests can be runned via Galaxy's `run_tests.sh`
 script. See the `README` file for each tool for more details.

In addition the same functional tests are runned via TravisCI whenever this 
GitHub repository is updated:

[![Build Status](https://travis-ci.org/ASaiM/galaxytools.svg)](https://travis-ci.org/ASaiM/galaxytools)

This TravisCI integration simulates a manual install of these Galaxy Tools and 
their dependencies. See the `.travis.yml` file for more technical details.

# Bugs

You can file an issue [here](https://github.com/ASaiM/galaxytools/issues).

# License

ASaiM Galaxy tool wrappers are released under Apache 2 License. See the LICENSE 
file for details
