# festive-lights
Python Script that runs an LED RGB light strip from a raspberry PI

Uses [rpi_ws281x example script](https://github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py) as a starting point

For use on a raspberry PI with the [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library installed

See the [Adafruit NeoPixels on RAspberry Pi Guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) for wiring.

## tmux

### Create

```sh
tmux new -s festive-lights
sudo python festive.py -c
```

### Detach

`ctrl`+`b` `d`

### Attach

```
tmux a -t [name of session]
```