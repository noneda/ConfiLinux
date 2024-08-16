Gpu=$(nvidia-smi | grep -P -o '[0-9]+(?=C)')
Cpu=$(sensors | grep "Package id 0:" | grep -Po '[0-9]+(.0°C=?)')

notify-send -r 73 "Temperature " "Cpu: ${Cpu:0:6}   Gpu: ${Gpu}.0°C"
