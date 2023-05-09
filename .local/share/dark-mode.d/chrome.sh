#!/bin/bash

flag="--force-dark-mode"
filename="$HOME/.config/chrome-flags.conf"

grep -e "$flag" "$filename" || sed -i "$ s/$/ $flag/" "$filename"
