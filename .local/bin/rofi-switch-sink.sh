#!/bin/bash
# rofi-switch-sink

set -e

function printoptions() {
    # Read to array
    mapfile -t sinks < <(pactl list sinks | awk -F': ' '/\s*Description:/ {print $2} /\sName:/ {print $2};')
    default_sink=$(pactl get-default-sink)
    len=${#sinks[@]}

    # Rofi prompt
    printf "\0prompt\x1fSelect PulseAudio Sink\n"

    # Individual options
    for (( j=0; j<len; j+=2)); do
        # Print option
        printf "%s\0info\x1f%s\n" "${sinks[$j+1]}" "${sinks[$j]}";
        # Mark the current option as selected and active
        if [[ "${sinks[$j]}" = "$default_sink" ]]; then
            printf "\0active\x1f%d\n" $((j / 2));
        fi
    done
}

nargs=$#
if ((nargs == 0)); then
    printoptions
    exit 0
else
    pactl set-default-sink "$ROFI_INFO"
fi