CD_HIT memory usage

ACD_HIT requires a certain amount of memory to perform the assembly.

By default, this tool is configured to limit the memory consumption to 6G. You might need to lower this limit if the machine(s) executing the jobs have less memory available. If you have a lot of reads to assemble and a machine with enough memory, you can increase it. In both cases, you can edit the CD_HIT_MEM_OPTIONS in the file:

<tool_dependency_dir>/environment_settings/CD_HIT_MEM_OPTIONS/bebatut/cdhit/<hash_string>/env.sh

to lower the maximum memory usage to 2G for example:

TRINITY_MEM_OPTIONS='--max_memory 2G --bflyHeapSpaceMax 2G'