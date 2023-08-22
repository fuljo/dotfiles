# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THEvscode-recent USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# pylint: disable=bare-except,invalid-name,missing-docstring

from pathlib import Path
import subprocess

from qtile_extras import widget
from libqtile import bar, hook, layout, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.backend.base import Window
from libqtile.backend.wayland import InputConfig
from libqtile.dgroups import simple_key_binder
from libqtile.log_utils import logger

mod = "mod4"
terminal = guess_terminal()

qtile_path = Path.home().joinpath(".config", "qtile")
rofi_path = Path.home().joinpath(".config", "rofi", "bin")
icon_font_name = "Font Awesome 6 Pro Regular"
commands = {
    "browser": "google-chrome-stable",
    "terminal": "alacritty",
    "files": "dolphin",
    "editor": "code",
    "launcher": "rofi -show drun",
    "window-switcher": "rofi -show window",
    "audio-switcher": "rofi -show audio-switcher",
    "powermenu": "rofi -show power-menu",
    "vscode-recent": "rofi -show vscode-recent",
    "emoji-selector": "rofi -show emoji -modi emoji",
    "bluetooth": "rofi-bluetooth",
    "screenshot": "flameshot gui",
    "suspend": "systemctl suspend",
}

match qtile.core.name:
    case "x11":
        commands["clipboard-manager"] = "clipmenu -p Clipboard"
        commands["lockscreen"] = "xset s activate"
        commands["layout-switcher"] = "rofi-autorandr"
    case "wayland":
        commands[
            "clipboard-manager"
        ] = "cliphist list | rofi -dmenu | cliphist decode | wl-copy"
        commands["lockscreen"] = "swaylock -f"
        commands["layout-switcher"] = ""  # TODO

colors = {
    "background": "#1a1b26",
    "foreground": "#a9b1d6",
    "active": "#ff9e64",
    "active-alt": "#449dab",
    "white": "#787c99",
    "black": "#32344a",
    "red": "#f7768e",
    "green": "#73daca",
    "yellow": "#f7dd8f",
    "orange": "#e0af68",
    "blue": "#7aa2f7",
    "magenta": "#ad8ee6",
    "cyan": "#7dcfff",
    "pink": "#fd96ff",
    "teal": "#0db9d7",
    "lime": "#b9c244",
    "brown": "#d99177",
    "indigo": "#698cd6",
    "gray": "#4b4e52",
    "blue-gray": "#444b6a",
    "dark-blue": "#3d59a1",
}

# colors_primary = {
#     "background": "#1a1b26",
#     "foreground": "#a9b1d6",
#     "separator": "#787c99"
# }

# colors_dark = {
#     "black":   "#02041a",
#     "red":     "#c7465e",
#     "green":   "#6e9e3a",
#     "yellow":  "#b07f38",
#     "blue":    "#4a72c7",
#     "magenta": "#7d5eb6",
#     "cyan":    "#146d7b",
#     "white":   "#7981a6",
# }

# colors_normal = {
#     "black":   "#32344a",
#     "red":     "#f7768e",
#     "green":   "#9ece6a",
#     "yellow":  "#e0af68",
#     "blue":    "#7aa2f7",
#     "magenta": "#ad8ee6",
#     "cyan":    "#449dab",
#     "white":   "#a9b1d6",
# }

# colors_bright = {
#     "black":   "#444b6a",
#     "red":     "#ff7a93",
#     "green":   "#b9f27c",
#     "yellow":  "#ff9e64",
#     "blue":    "#7da6ff",
#     "magenta": "#bb9af7",
#     "cyan":    "#0db9d7",
#     "white":   "#e5e5e5",
# }

###################
# Keys
###################
keys = []

# Navigation
keys += [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.client_to_previous(),
        desc="Move window to previous stack",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.client_to_next(),
        desc="Move window to next stack",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.client_to_previous(),
        desc="Move window to previous stack",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.client_to_next(),
        desc="Move window to next stack",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window right"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle folating
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating window"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Space", lazy.next_layout(), desc="Toggle between layouts"),
    # Switch screen
    Key([mod], "comma", lazy.prev_screen(), desc="Switch focus to previous screen"),
    Key([mod], "period", lazy.next_screen(), desc="Switch focus to next screen"),
    Key([mod], "less", lazy.next_screen(), desc="Switch focus to next screen"),
]

# Launch apps
keys += [
    Key([mod], "Return", lazy.spawn(commands["terminal"]), desc="Launch terminal"),
    Key(
        [mod],
        "a",
        lazy.spawn(commands["window-switcher"]),
        desc="Launch window switcher",
    ),
    Key([mod], "b", lazy.spawn(commands["browser"]), desc="Launch web browser"),
    Key(
        [mod, "mod1"],
        "b",
        lazy.spawn(commands["bluetooth"]),
        desc="Launch bluetooth menu",
    ),
    Key([mod], "c", lazy.spawn(commands["vscode-recent"]), desc="Launch code editor"),
    Key([mod], "d", lazy.spawn(commands["launcher"]), desc="Show application launcher"),
    Key([mod], "e", lazy.spawn(commands["files"]), desc="Launch file explorer"),
    Key(
        [mod],
        "p",
        lazy.spawn(commands["layout-switcher"]),
        desc="Launch display layout switcher",
    ),
    Key(
        [mod, "mod1"],
        "a",
        lazy.spawn(commands["audio-switcher"]),
        desc="Launch PulseAudio sink switcher",
    ),
    Key([mod, "mod1"], "l", lazy.spawn(commands["lockscreen"]), desc="Lock screen"),
    Key([mod], "s", lazy.spawn(commands["screenshot"]), desc="Take screenshot"),
    Key(
        [mod],
        "x",
        lazy.spawn(commands["clipboard-manager"]),
        desc="Open clipboard manager",
    ),
    Key([mod], "period", lazy.spawn(commands["emoji-selector"]), desc="Launch emoji selector"),
    Key([mod], "Escape", lazy.spawn(commands["powermenu"]), desc="Launch power menu"),
]

# Qtile
keys += [
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Groups

keys += [
    Key(
        [mod],
        "t",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle dropdown termial",
    ),
]

# Special keys
keys += [
    # Audio Volume
    Key([], "XF86AudioMute", lazy.spawn("volume.sh toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume.sh 2%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume.sh 2%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioPause", lazy.spawn("playerctl pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightness.sh -l -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightness.sh -l -U 5")),
    Key([], "XF86KbdBrightnessUp", lazy.spawn("brightness.sh -k -A 1")),
    Key([], "XF86KbdBrightnessDown", lazy.spawn("brightness.sh -k -U 1")),
    # Other
    Key([], "XF86ScreenSaver", lazy.spawn(commands["lockscreen"])),
    Key([], "XF86Sleep", lazy.spawn(commands["suspend"])),
    # Key([], "XF86TouchpadToggle", lazy.spawn("")),
    Key([], "XF86Calculator", lazy.group["scratchpad"].dropdown_toggle("octave")),
    Key([], "Print", lazy.spawn(commands["screenshot"]), desc="Take screenshot"),
]

###################
# Groups
###################

groups = [
    Group(
        "DEV",
        label="\uf121",
        layout="max",
        matches=[Match(wm_class=["Code", "jetbrains-clion", "jetbrains-idea-ce"])],
    ),
    Group(
        "WWW", label="\uf0ac", layout="max", matches=[Match(wm_class=["google-chrome"])]
    ),
    Group("CLI", label="\uf120", layout="columns"),
    Group(
        "DOC",
        label="\uf044",
        layout="max",
        matches=[Match(wm_class=["okular", "Zathura", "libreoffice", "libreoffice-writer", "libreoffice-calc", "libreoffice-impress"])],
    ),
    Group(
        "SYS", label="\uf07b", layout="columns", matches=[Match(wm_class=[
            "dolphin", "pavucontrol", "easyeffects", "systemsettings"])]
    ),
    Group(
        "CHAT",
        label="\uf075",
        layout="max",
        matches=[
            Match(
                wm_class=[
                    "discord",
                    "telegram-desktop",
                    "web.whatsapp.com",
                    "crx_cifhbcnohmdccbgoicgdjpfamggdegmo", # PWA for Teams
                    "crx_kjgfgldnnfoeklkmfkjfagphfepbbdan", # PWA for Meet
                ]
            )
        ],
    ),
    Group(
        "MEDIA",
        label="\uf144",
        layout="max",
        matches=[
            Match(
                wm_class=[
                    "spotify",
                    "lollypop",
                    "vlc",
                    # PWA for Youtube
                    "crx_agimnkijcaahngcdmfeangaknmldooml",
                ]
            )
        ],
    ),
    Group(
        "GFX",
        label="\uf03e",
        layout="max",
        matches=[Match(wm_class=["Inkscape", "gimp-2.10", "obs"])],
    ),
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", terminal),
            DropDown("octave", f"{terminal} -e octave"),
            DropDown(
                "cal-1",
                f"{terminal} --hold -e cal -m -1",
                height=0.2,
                width=0.12,
                x=0.87,
            ),
            DropDown(
                "cal-3",
                f"{terminal} --hold -e cal -m -3",
                height=0.2,
                width=0.36,
                x=0.63,
            ),
        ],
    ),
]

###################
# Layouts
###################

layout_theme = {
    "border_normal": colors["background"],
    "border_focus": colors["dark-blue"],
}

layout_borders = {
    "border_width": 2,
    "margin": 8,
}

layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme, **layout_borders),
    layout.Stack(num_stacks=2, **layout_theme, **layout_borders),
    layout.Columns(**layout_theme, **layout_borders),
    layout.Floating(**layout_theme, **layout_borders),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

###################
# Bar
###################

widget_defaults = dict(
    font="Cascadia Code PL",
    fontsize=13,
    padding=5,
    background=colors["background"],
    foreground=colors["foreground"],
    icon_theme="Papirus-Dark",
    menu_background=colors["background"],
    menu_foreground=colors["foreground"],
    menu_font="Cascadia Code PL",
    menu_fontsize=13,
    separator_colour=colors["blue-gray"],
)
extension_defaults = widget_defaults.copy()
bar_height = 32
icon_size = 15
powerline_left = "\ue0b2"


def make_separator(**kwargs):
    return widget.TextBox(
        text="|",
        foreground=colors["blue-gray"],
        fontsize=14,
        **kwargs,
    )


def make_icon(text, foreground, **kwargs):
    return widget.TextBox(
        text=text,
        foreground=foreground,
        font=icon_font_name,
        fontsize=icon_size,
        padding=3,
        **kwargs,
    )

def make_tray(**kwargs):
    match qtile.core.name:
        case "x11":
            logger.info("Using X11 tray")
            return widget.Systray(**kwargs)
        case "wayland":
            logger.info("Using Wayland tray")
            return widget.StatusNotifier(**kwargs)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font=icon_font_name,
                    fontsize=icon_size,
                    active=colors["foreground"],
                    inactive=colors["blue-gray"],
                    highlight_color=colors["black"],
                    highlight_method="line",
                    this_current_screen_border=colors["active"],
                    this_screen_border=colors["active"],
                    other_screen_border=colors["active-alt"],
                ),
                make_separator(),
                widget.CurrentLayoutIcon(
                    scale=0.61,
                    foreground=colors["foreground"],
                    use_mask=True,
                ),
                widget.CurrentLayout(),
                make_separator(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": (colors["red"], colors["white"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                make_separator(),
                # System tray
                make_tray(),
                make_separator(),
                # CPU
                make_icon(
                    "\uf2db",
                    colors["blue"],
                ),
                widget.CPU(
                    format="{load_percent:4.01f}%",
                    padding=5,
                    foreground=colors["yellow"],
                ),
                # Memory
                widget.Memory(
                    format="{MemUsed:.02f}/{MemTotal:.0f} GB",
                    measure_mem="G",
                    padding=5,
                    foreground=colors["yellow"],
                ),
                make_separator(),
                # Network
                make_icon(
                    "\uf1eb",
                    colors["pink"],
                ),
                widget.Net(
                    interface=None,
                    format="{down} ↓↑ {up}",
                    padding=5,
                    foreground=colors["green"],
                ),
                make_separator(),
                # Thermal sensor
                make_icon(
                    "\uf2c9",
                    colors["red"],
                ),
                widget.ThermalSensor(
                    format="{temp:.0f}{unit}",
                    gpu_bus_id="1:00.0",
                    foreground=colors["foreground"],
                    foreground_alert=colors["red"],
                    padding=5,
                ),
                # GPU
                widget.NvidiaSensors(
                    format="{temp}°C",
                    foreground=colors["foreground"],
                    foreground_alert=colors["red"],
                    padding=5,
                ),
                make_separator(),
                # Backlight
                make_icon(
                    "\uf186",
                    colors["lime"],
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    change_command="brightness.sh -S {0}",
                    padding=5,
                    foreground=colors["blue"],
                ),
                make_separator(),
                # Volume
                make_icon(
                    "\uf6a8",
                    colors["green"],
                ),
                widget.Volume(
                    fmt="{}",
                    padding=5,
                    foreground=colors["magenta"],
                ),
                # Media player
                make_icon(
                    "\uf001",
                    colors["green"],
                ),
                widget.Mpris2(
                    display_metadata=["xesam:artist", "xesam:title"],
                    width=128,
                    scroll=True,
                    padding=5,
                    foreground=colors["magenta"],
                ),
                make_separator(),
                # Updates
                make_icon(
                    "\uf1b2",
                    colors["brown"],
                ),
                widget.CheckUpdates(
                    colour_have_updates=colors["yellow"],
                    colour_no_updates=colors["blue-gray"],
                    display_format="{updates}",
                    distro="Arch_yay",
                    initial_text="-",
                    no_update_string="0",
                    padding=5,
                ),
                make_separator(),
                # Clock
                make_icon(
                    "\uf133",
                    colors["pink"],
                ),
                widget.Clock(
                    format="%a %d/%m/%Y",
                    foreground=colors["cyan"],
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle("cal-1"),
                        "Button3": lazy.group["scratchpad"].dropdown_toggle("cal-3"),
                    },
                ),
                make_icon(
                    "\uf017",
                    colors["pink"],
                ),
                widget.Clock(
                    format="%H:%M",
                    foreground=colors["cyan"],
                ),
                widget.TextBox(),
            ],
            bar_height,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
    )
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Autostart
@hook.subscribe.startup_once
def autostart():
    subprocess.run(str(qtile_path.joinpath("autostart.sh")), check=True)


dgroups_key_binder = simple_key_binder(mod)
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    **layout_borders,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="itunes.exe"),
        Match(title="plasma-emojier"), # emoji selector
        # Match(func=lambda w: w.window.get_wm_transient_for()),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
    "type:keyboard": InputConfig(kb_layout='it'),
}

# Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
