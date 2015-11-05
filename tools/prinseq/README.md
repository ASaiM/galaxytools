Galaxy wrapper for PRINSEQ
===========================

PRINSEQ is a tool for easy and rapid quality control and data processing of 
metagenomic and metatranscriptomic datasets. This tool allow to process the 
sequences with filtering and trimming. For more information, check the 
[user manual](http://prinseq.sourceforge.net/manual.html)

# Installation

## Automated installation

On a Galaxy instance, the wrapper can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tool and data, ...

## Manual installation

For manual installation, the files `prinseq.xml` must be put in the `tools/prinseq/`
 folder and add the XML files to Galaxy's `tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="Control quality" id="prinseq">
    <tool file="prinseq/prinseq.xml" />
</section>
```

PRINSEQ must be installed somewhere on the system path. 

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid prinseq
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff --shed_target ~/repositories/galaxytools/tools/prinseq/
```

or:

```
planemo shed_update -t toolshed --check_diff --shed_target ~/repositories/galaxytools/tools/prinseq/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details