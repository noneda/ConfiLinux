from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"

keys = [
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod , "mod1"], "Return", lazy.layout.toggle_split()),
    #Add Other
    Key([mod], "m", lazy.spawn("""rofi -show drun --icon-theme "Fluent grey dark" -show-icons """), desc="Open Menu Rofi"), 
    Key([mod], "n", lazy.spawn("""rofi -show window -icon-theme "Fluent grey dark" -show-icons"""), desc="Open Menu Rofi"),
    Key([mod], "f", lazy.spawn("discord"), desc="Open Firefox"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Open Files Manager"),
    Key([mod], "a", lazy.spawn("vivaldi-stable"), desc="Open Vivaldi"),
    Key([mod], "s", lazy.spawn("google-chrome-stable"), desc="Open Google"),
    Key([mod, "shift"], "a", lazy.spawn("firefox"), desc="Open Google"),
    Key([mod], "d", lazy.spawn("code"), desc="Open Vivaldi"),
    Key([mod], "o", lazy.spawn("gogglesmm"), desc="Open Music"),
    Key([mod], "g", lazy.spawn("pamac-manager"), desc="Open Music"),
    

    Key([],"XF86MonBrightnessDown", lazy.spawn(
        """sh /home/noneda/.config/scripts/brighMin.sh"""
    ),desc="Uo brightnes"),

    Key([], "XF86MonBrightnessUp",  lazy.spawn(
        """sh /home/noneda/.config/scripts/brighSup.sh"""
    ),desc="Down brightnes"),

    Key([mod , "shift"],"d", 
    lazy.spawn(
        """dunstctl close-all"""
        ),desc= "Close All Notifications"),
    Key([mod],"t" ,lazy.spawn(
        """sh /home/noneda/.config/scripts/ShowInfo.sh"""
        ), desc= "Show Temperature"
        ),

    Key([], "XF86AudioRaiseVolume",lazy.spawn(
    """sh /home/noneda/.config/scripts/AudioSup.sh"""
    ),desc="Up Volumen"),

    Key([], "XF86AudioLowerVolume",lazy.spawn(
    """sh /home/noneda/.config/scripts/AudioMin.sh"""
        ),desc="Up Volumen"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s /home/noneda/Pictures/Screens/Screen.png"), desc = "Screen"),

    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal kitty"),
    Key([mod, "shift"], "Return", lazy.spawn("alacritty"), desc="Launch terminal Alacritty"),


    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
