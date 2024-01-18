import os
from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from libqtile.lazy import lazy


ColorShame = ["#515A5A","#16A085","#17A589","#DAF7A6","#FFC300", "#FF5733"]


colors = [
    "#0E6655",
    "#7DCEA0",
    "#273746",
    "#515A5A", 
    "#EAECEE"
] 


def Space_w(fg):
    return widget.TextBox(
        text = "",
        fontsize = 22,
        foreground = fg,
        background = "#00000000",
        padding = -1,
    )
def  Space_r(fg):
    return widget.TextBox(
        text = "",
        fontsize = 22,
        foreground = fg,
        background = "#00000000",
        padding = -1,
    )

screens = [
    Screen(
        wallpaper= '/home/Arlz/Pictures/Pictures/heeee_noice.jpg',
        wallpaper_mode='fill',
        # bottom=bar.Bar(
        top=bar.Bar(
        [
            widget.Spacer (
                length = 50
            ),
            Space_r(
                fg = colors[0]
            ),
            widget.TextBox(
                mouse_callbacks = {'Button1' : lazy.spawn("""rofi -show drun --icon-theme "Fluent grey dark" -show-icons """)},
                background = colors[0], 
                foreground = "#ffffff",
                text =  "", 
                fontsize = 15,
                ),
            Space_w(
                fg = colors[0]
            ),
            widget.Spacer(
                
            ),
            
            Space_r(
                   fg = ColorShame[2]
                    ),
            widget.Clock(
                format=" %Y-%m-%d %a 󰥔 %H:%M",
                background = ColorShame[2],
                foreground = "#fff" 
            ),
            Space_w(
                fg = ColorShame[2]
            ),
            widget.Spacer(

            ),
            widget.TextBox(
                text = "",
                fontsize = 22,
                foreground = "#FDFEFE",
                background = "#00000000",
                padding = -1
            ),
            widget.Systray( 
                background = "#00000000", padding = 7, icon_size = 18
            ),

            widget.TextBox(
                text = "",
                fontsize = 22,
                foreground = "#FDFEFE",
                background = "#00000000",
                padding = -1
            ),
            widget.Spacer(

            ),
        
            Space_r(
                fg = "#34495E"
            ),
             widget.GroupBox(
                margin_y = 3,
                active="#A3E4D7",
                disable_drag = True,
                fontsize = 19,
                highlight_method = 'text',
                inactive = "#ffffff",
                this_current_screen_border = "#16A085",
                background = "#34495E",
                
            ),  
            Space_w(
                fg = "#34495E"
            ), 
            widget.Spacer(

            ),
            Space_r (
                fg = colors[4]
            ),
            widget.Wlan(
                background = colors[4], format = ' ', interface =  'wlp0s20f3',
                foreground = "#282a36", disconnected_message = "󰤯 ",
                mouse_callbacks = {'Button1' : lazy.spawn("kitty nmtui")}
            ),
#            widget.Bluetooth(
#                background = colors[4], fmt = '{}', foreground = "#282a36"
#            ),
            widget.CheckUpdates(
                background = colors[4],
                colour_have_updates ="#282a36",
                colour_no_updates ="#282a36",
                no_update_string = "",
                update_interval = 3600,
                distro = 'Arch', 
                display_format = '',
                mouse_callbacks = {'Button1' : lazy.spawn("kitty sudo pacman -Syu")}
            ),
            Space_w (
                fg = colors[4]
            ),

            widget.Spacer(

            ),
            Space_r(
                fg = ColorShame[1]
            ),
            widget.PulseVolume(
                    background = ColorShame[1], limit_max_volume = True, fmt = ' {} ', device='default',
                    ),
            widget.Battery(
                    background = ColorShame[1],
                    charge_char = '',discharge_char = '',full_char = '',
                    update_interval = 1, unknow_char = '', 
                    low_foreground = "#A93226",low_percentaje = 0.9,
                    format = ' {char} {percent:2.0%}' 
                    ),
            Space_w(
                fg = ColorShame[1]
            ),
            widget.Spacer(

            ),
            Space_r (
                fg = "#273746"
            ),
            widget.CurrentLayoutIcon(
                background = "#273746", 
                scale = 0.66, padding = 5, fmt = '{} '
            ),
            widget.QuickExit(
                fontsize = 16 , background = "#273746", 
                countdown_format = ' ',default_text = '', 
                fmt = ' {}' , 
            ),
            Space_w (
                fg = "#273746"
            ),
            widget.Spacer (
                length = 50
            )
        ],
            20,
            background= "#00000000",
            opacity = 0.9,
            margin=[10,6,4,6],
            # margin=[4,4,6,4],
            # opacity=0.79,
        ),
    ),
]
