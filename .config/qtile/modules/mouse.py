from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from .keys import mod

mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod, "shift"], "Button3", lazy.window.bring_to_front()),
        Click([mod, "shift"], "Button1",lazy.window.disable_floating()), 
        #Click([mod, "control"], "Button1", lazy.window.set_opacity(), start=lazy.down_opacity()),
        #Click([mod, "control"], "Button3", lazy.window.set_opacity(), start=lazy.up_opacity()),
]