#!/usr/bin/env bash

INDEXPATH=$HOME/.local/share/ulauncher/extensions/ulauncher-file-search/

if [[ -x "$(command -v python)"  ]]; then
    python $INDEXPATH
else
    python3 $INDEXPATH
fi

exit 0

