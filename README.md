# [fuljo](https://github.com/fuljo)'s dotfiles

This repo contains my dotfiles for my Manjaro install.

### Theme

- I mainly use the Tokyo Night theme (inspired by [this](https://github.com/enkia/tokyo-night-vscode-theme)). This is already configured for Qt and GTK apps.
- My main coding font is [Cascadia Code](https://github.com/microsoft/cascadia-code)

### System

- [Qtile](https://github.com/qtile/qtile) as window manager with X11.
- A configuration for [i3](https://i3wm.org/) is also available, but I haven't finished it.
- [picom](https://github.com/yshui/picom) as compositor.
- [Rofi](https://github.com/davatorium/rofi) as launcher, application switcher, shutdown menu and [recent menu for VSCode](https://github.com/fuljo/rofi-vscode-mode).
- [Dunst](https://github.com/dunst-project/dunst) for notifications.
- [Gammastep](https://gitlab.com/chinstrap/gammastep) for night gamma correction (redshift).
- [Betterlockscreen](https://github.com/betterlockscreen/betterlockscreen) under [xss-lock](https://github.com/google/xsecurelock) for screen locking.
- [Darkman](https://gitlab.com/WhyNotHugo/darkman) for night mode switching.

### Applications

- [Alacritty](https://github.com/alacritty/alacritty) as terminal emulator.
- [Flameshot](https://flameshot.org/) as screenshot tool.
- [Git](https://git-scm.com/) with some configured aliases.

## Installation

First [install yadm](https://yadm.io/docs/install) on your system
```sh
pacman -S yadm
```

Then clone the repo locally:
```sh
yadm clone https://github.com/fuljo/dotfiles
yadm status
```
and solve any merge conflicts.