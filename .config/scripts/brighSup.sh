VarLuz=$(brightnessctl i | grep -P -o '[0-9]+(?=%)') 

if [[ $VarLuz -eq 100 ]]; then
  notify-send -r 832 "Brightness: Maximum" "          $VarLuz"
  else
    brightnessctl set 5+%
    VarLuz=$(brightnessctl i | grep -P -o '[0-9]+(?=%)')
  notify-send -r 832 "Brightness +5" "         $VarLuz"
fi
