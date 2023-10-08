#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

[[ -f ~/.profile ]] && . ~/.profile

# SSH key agent
# if ! pgrep -u "$USER" ssh-agent > /dev/null; then
#     ssh-agent -t 1h > "$XDG_RUNTIME_DIR/ssh-agent.env"
# fi
# if [[ ! "$SSH_AUTH_SOCK" ]]; then
#     export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
# fi

# Desktop session
# if [ -n "${XDG_SESSION_DESKTOP-}" ]; then
    # Keyboard
    # export XKB_DEFAULT_LAYOUT='it'
    # export XKB_DEFAULT_MODEL='pc105'

    # SSH
    # export SSH_ASKPASS='/usr/bin/ksshaskpass'
    # export SSH_ASKPASS_REQUIRE=prefer

    # Qt
    # if [[ "$XDG_CURRENT_DESKTOP" != 'KDE' ]]; then
    #     export QT_QPA_PLATFORMTHEME='qt5ct'
    # fi
    
    # Update dbus and systemd environment
    # if [[ "$XDG_SESSION_TYPE" == 'wayland' ]]; then
    #     dbus-update-activation-environment --systemd \
    #         DISPLAY=':1' WAYLAND_DISPLAY='wayland-0' XAUTHORITY="$HOME/.Xauthority"\
    #         XDG_SESSION_DESKTOP XDG_CURRENT_DESKTOP XDG_SESSION_TYPE \
    #         QT_QPA_PLATFORM QT_QPA_PLATFORMTHEME
    # fi
# fi
