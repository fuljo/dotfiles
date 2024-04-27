#!/usr/bin/env bash
export QT_QPA_PLATFORMTHEME="qt5ct"
export EDITOR=/usr/bin/vim
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
# fix "xdg-open fork-bomb" export your preferred browser from here
export BROWSER=/usr/bin/google-chrome-stable

# Docker
export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock

# MPI
export OMPI_MCA_btl_tcp_if_include=lo
export OMPI_MCA_mpi_yield_when_idle=1

# Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Development
source /usr/bin/virtualenvwrapper.sh

# SSH key agent
if [[ ! "$SSH_AUTH_SOCK" ]]; then
    export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/gcr/ssh"
fi

# Rofi
#export ROFI_VSCODE_FLAVOR=code-oss
#export ROFI_VSCODE_ICON_MODE=none
export ROFI_VSCODE_ICON_FONT="Cascadia Code PL"
export ROFI_VSCODE_ICON_COLOR="#c0caf5ff"

# Clipmenu
export CM_MAX_CLIPS=10
export CM_SELECTIONS="clipboard primary"
export CM_IGNORE_WINDOW="Ksshaskpass|Wallet Manager|pinentry|seahorse"
export CM_LAUNCHER="rofi"

