from libqtile import bar
from .widgets import *
from libqtile.config import Screen

ColorShame = ["#515A5A","#16A085","#17A589","#DAF7A6","#FFC300", "#FF5733"]
Border = ["#909497", "#616A6B"]

def Space_w(fg, bg):
    return widget.TextBox(
        text = "",
        fontsize = 20,
        foreground = fg,
        background = bg,
        padding = -1,
    )



screens = [
    Screen(
        wallpaper= '/home/Arlz/Pictures/Pictures/heeee_noice.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.TextBox(
                    background = "#7DCEA0", 
                    foreground = "#ffffff",
                    text =  "  ", 
                    fontsize = 15,
                   ),
                Space_w(
                    bg = "#34495E" , fg = "#7DCEA0"
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
                    bg = "#D5D8DC" , fg = "#34495E" 
                    ),
                widget.WindowCount(
                    foreground = "#34495E",
                    fontsize = 14 ,
                    fmt = '  {}',
                    background = "#D5D8DC",
                    ),
                widget.WindowName(
                    foreground = "#34495E",
                    fontsize = 13,
                    fmt = '   {}',
                    background = "#D5D8DC"
                    ),
                Space_w(
                    fg = "#D5D8DC" , bg = ColorShame[0]
                    ),
                 widget.Systray( 
                               background = ColorShame[0], padding = 1
                               ),
                Space_w(
                        fg = ColorShame[0], bg = ColorShame[2]
                        ),
                
                widget.Wlan(
                        foreground = ColorShame[3], background = ColorShame[2], format = '  {essid}{percent: 2.0%} ', interface =  'wlp0s20f3'
                        ),
                widget.CheckUpdates(
                        colour_no_updates = ColorShame[3],
                        colour_have_updates = ColorShame[3],
                        background = ColorShame[2],
                        no_update_string = "  ",
                        update_interval = 3600,
                        distro = 'Arch', 
                        display_format = '  '
                        ),
                Space_w (
                        bg = ColorShame[4], fg = ColorShame[2]
                        ),
                widget.Clock(
                        format=" %Y-%m-%d %a 󰥔 %H:%M",
                        background = ColorShame[4],
                        foreground = "#5D6D7E" ),
                Space_w (
                        bg = ColorShame[5], fg = ColorShame[4]
                        ),
                widget.PulseVolume(
                       background = ColorShame[5], limit_max_volume = True, fmt = ' {} ', device='default'
                       ),
                widget.Battery(
                        background = ColorShame[5],
                        charge_char = '',discharge_char = '',full_char = '', update_interval = 1, unknow_char = '', 
                        low_foreground = "#A93226",low_percentaje = 0.9,
                                format = ' {char} {percent:2.0%}' 
    ,
                    ),
                Space_w(
                        fg = ColorShame[5], bg = ColorShame[2] 
                        ),
                widget.CurrentLayoutIcon(
                        background = ColorShame[2],
                        scale = 0.6, padding = 0, fmt = '{} '
                        ),
                widget.QuickExit(
                        fontsize = 16 ,background = ColorShame[2],countdown_format = ' ',default_text = '', fmt = ' {} ' 
                        ),
            ],
            19,
            background="#282a36" ,
            opacity=0.95,
            margin= [ 7,8,7,8],
        ),
    ),
]
