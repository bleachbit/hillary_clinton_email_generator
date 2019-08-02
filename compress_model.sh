#!/bin/bash

# Copyright (C) 2019 by Andrew Ziem.  All rights reserved.
# License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
# This is free software: you are free to change and redistribute it.
# There is NO WARRANTY, to the extent permitted by law.
#
# Compress models for distribution
#

for model in content subject; do
    echo processing $model
    BASENAME=${model}_model.json
    echo basename=${BASENAME}
    rm -f json.tmp ${BASENAME}.bz2
    echo Size before:
    ls -la ${BASENAME} || exit 1
    jq -c . < ${BASENAME} > json.tmp || exit 1
    mv json.tmp ${BASENAME} || exit 1
    rm -f json.tmp
    echo Size before jq:
    ls -la ${BASENAME}
    bzip2 --keep --best ${BASENAME} || exit 1
    mv ${BASENAME}.bz2 clinton_${BASENAME}.bz2
done


