#!/bin/sh
#
#Configuracion Teclado Spanish Latam
setxkbmap latam &
sudo ntpd -qg &
#Resolucion de Pantalla
#Tengo Problemas con eso por el Momento
#nitrogen --restore &
picom &
redshift -P -O 4500K &
syndaemon -i 0.5 -d
#xrandr -s 1920x1080 -r 60.0 &
#xrandr --output eDP-1 --mode 1920x1080 --rate 60.01
#optimus-manager --switch hybrid &

