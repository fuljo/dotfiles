#!/bin/bash

flag="--force-dark-mode"
filename="$HOME/.config/chrome-flags.conf"

sed -i "s/ $flag//g" "$filename"
