CD_HIT memory usage
====================

By default, maximum of 4Gb is attributed to CD_HIT.

To change the maximum memory usage, you can edit the CD_HIT_MEM_OPTIONS in the file:

<tool_dependency_dir>/cd-hit/4.6.4/bebatut/cdhit/<hash_string>/env.sh

For example to increase to 8Gb, you will write:

CD_HIT_MEM_OPTIONS='-M 8000'