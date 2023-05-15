#!/bin/bash
# changeVolume

# Arbitrary but unique message tag
msgTag="myvolume"

# Change the volume using amixer
device="default"
control="Master"
status="$(amixer -D $device set $control "$@")"

# Query pulseaudio for the current volume and whether or not the speaker is muted
volume="$(echo "$status" | grep -o -m 1 -P '(?<=\[)[0-9]*(?=%\])')"
out_muted="$(echo "$status" | grep -o -m 1 -P '(?<=\[off\])')"
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