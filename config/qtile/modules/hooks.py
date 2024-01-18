from libqtile import hook
import subprocess
import os

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/scripts/autostart.sh'])