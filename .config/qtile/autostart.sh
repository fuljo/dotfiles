#!/usr/bin/env bash

# Set variables in the systemd user environment
case "$XDG_SESSION_TYPE" in
    wayland)
        systemctl --user import-environment DISPLAY WAYLAND_DISPLAY SWAYSOCK XDG_CURRENT_DESKTOP
        hash dbus-update-activation-environment 2>/dev/null && \
        dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY SWAYSOCK XDG_CURRENT_DESKTOP
        ;;
esac

# Create default user directories
xdg-user-dirs-update &

# Monitor configuration
case "$XDG_SESSION_TYPE" in
    x11)
        autorandr --change &
        ;;
    wayland)
        kanshi &
        ;;
esac

# Compositor
case "$XDG_SESSION_TYPE" in
    x11)
        picom &
        ;;
esac

# Notification manager
case "$XDG_SESSION_TYPE" in
    x11)
        dunst &
        ;;
    wayland)
        mako &
        ;;
esac

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

# Mounting daemon
if [[ -x "$(command -v pcmanfm)" ]]; then
    pcmanfm -d &
fi

# KDE Wallet
if [[ -x "/usr/lib/pam_kwallet_init" ]]; then
    /usr/lib/pam_kwallet_init &
fi

# NetworkManger Applet
nm-applet --indicator &

# Manjaro Settings Manager notifier
if [[ -x "$(command -v msm_kde_notifier)" ]]; then
    msm_kde_notifier &
fi

# Manjaro tray
if [[ -x "$(command -v matray)" ]]; then
    matray --delay &
fi

# Solaar
solaar --window=hide &

# MPRIS controller
playerctld daemon &

# Power alert daemon
if [[ -x "$(command -v poweralertd)" ]]; then
    poweralertd -s -i "line power" &
fi

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
