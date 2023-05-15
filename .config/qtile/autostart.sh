#!/usr/bin/env bash

export PATH="$HOME/.local/bin:$PATH"

# Monitor configuration
case "$XDG_SESSION_TYPE" in
    x11)
        autorandr --change &
        ;;
    wayland)
        # kanshi &
        ;;
esac

# Compositor
case "$XDG_SESSION_TYPE" in
    x11)
        picom &
        ;;
esac

# Notification manager
dunst &

# Redshift gamma correction
gammastep &

# PipeWire sound effects
easyeffects --gapplication-service &

# PulseAudio Systray
pasystray &

# Clipboard manager
case "$XDG_SESSION_TYPE" in
    x11)
        clipmenud &
        ;;
    wayland)
        wl-paste --watch cliphist store &
        ;;
esac

# KDE Wallet
/usr/lib/pam_kwallet_init &

# NetworkManger Applet
nm-applet --indicator &

# Manjaro Settings Manager notifier
msm_kde_notifier &

# Manjaro tray
matray --delay &

# Solaar
solaar --window=hide &

# MPRIS controller
playerctld daemon &

# Wallpaper
wp_1="/mnt/d/Graphics/vincenttrinidad/bountea-hunter.jpg"
wp_2="/mnt/d/Graphics/vincenttrinidad/the-great-starry-wave.jpg"
case "$XDG_SESSION_TYPE" in
    x11)
        feh --bg-max $wp_1 $wp_2 &
        ;;
    wayland)
        swaybg -i $wp_1 -m fit &
        ;;
esac

# Lockscreen
case "$XDG_SESSION_TYPE" in
    x11)
        xss-lock --transfer-sleep-lock -- betterlockscreen -l -- --nofork &
        ;;
    wayland)
        # TODO
        # swayidle \
        #     timeout 5 "qtile cmd-obj -o core -f hide_cursor" \
        #     resume "qtile cmd-obj -o core -f unhide_cursor" \
        #     timeout 300 "swayidle-laptop-dim" \
        #     resume "light -I" \
        #     timeout 600 "wlopm --off \*;swaylock -F -i ~/.cache/wallpaper --effect-blur 10x5 --clock --indicator" \
        #     resume "wlopm --on \*" &
        ;;
esac
