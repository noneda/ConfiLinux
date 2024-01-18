from libqtile import layout
from libqtile.config import Match


Border = ["#909497", "#616A6B"]
layouts = [
    layout.Bsp(
        border_focus = Border[0],
        border_normal = Border[1],
        border_width = 1,
        margin= 7,
        ),
    layout.Floating(
        border_focus = Border[0],
        border_normal = Border[1],
        border_width = 1,
        ),      
    layout.Max(
        margin = 7
        ),
]


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)