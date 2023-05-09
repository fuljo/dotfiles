#!/bin/bash
# changeVolume

# Usage: see pulseaudio-ctl

# Arbitrary but unique message tag
msgTag="myvolume"

# Change the volume using pulseaudio
# amixer -c 0 set Master "$@" > /dev/null
pulseaudio-ctl $@ > /dev/null

# Query pulseaudio for the current volume and whether or not the speaker is muted
status="$(pulseaudio-ctl full-status)"
volume="$(cut -f 1 -d' ' <<< ${status})"
out_muted="$(cut -f 2 -d' ' <<< ${status})"
in_muted="$(cut -f 3 -d' ' <<< ${status})"
if [[ $volume == 0 || "$out_muted" == "yes" ]]; then
    # Show the sound muted notification
    dunstify -a "changeVolume" -u low -i audio-volume-muted -h string:x-dunst-stack-tag:$msgTag "Volume muted" 
else
    # Show the volume notification
    dunstify -a "changeVolume" -u low -i audio-volume-high -h string:x-dunst-stack-tag:$msgTag \
    -h int:value:"$volume" "Volume: ${volume}%"
fi

# Play the volume changed sound
canberra-gtk-play -i audio-volume-change -d "changeVolume"