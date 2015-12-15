Galaxy wrapper for HUMAnN2
==========================

HUMAnN is a pipeline for efficiently and accuretly profiling the presence/absence 
and abundance of microbial pathways in a community from metagenomic or 
metatranscriptomic sequencing data. For more information, check the 
[user manual](http://huttenhower.sph.harvard.edu/humann2/manual)

# Installation

## Automated installation

On a Galaxy instance, the wrapper can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tool and data, ...

## Manual installation

For manual installation, the files `humann2.xml` must be put in the `tools/humann2/`
 folder and add the XML files to Galaxy's `tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="Profile microbial pathways in a community" id="humann2">
    <tool file="humann2/humann2.xml" />
</section>
```

MetaPhlAn2 must be installed somewhere on the system path. It can be done using:

```
planemo dependency_script ~/repositories/galaxytools/tools/humann2/
bash dep_install.sh
source env.sh
```

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid humann2
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff ~/repositories/galaxytools/tools/humann2/
```

or:

```
planemo shed_update -t toolshed --check_diff ~/repositories/galaxytools/tools/humann2/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details