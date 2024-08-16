Value=$(pactl list sinks | grep "Volume:" | grep -Po '[0-9]+(?=%)')
Data=${Value:0:3}
Date=${Value:0:2}
if [[ $Data -ge 100 ]]; then
    notify-send -r 501 "Volumen Full" "         100%"
    pactl set-sink-volume @DEFAULT_SINK@ 100%
    else
  if [[ $Data -lt 100 && $Date -ge 10  ]]; then
    pactl set-sink-volume @DEFAULT_SINK@ +5%
    Value=$(pactl list sinks | grep "Volume:" | grep -Po '[0-9]+(?=%)')
    notify-send -r 501 "Volumen +5" "       ${Value:0:3}"
    else
      pactl set-sink-volume @DEFAULT_SINK@ +5%
      Value=$(pactl list sinks | grep "Volume: " | grep -Po '[0-9]+(?=%)')
      notify-send -r 501 "Volumen +5" "       ${Value:0:2}"
  fi

fi


