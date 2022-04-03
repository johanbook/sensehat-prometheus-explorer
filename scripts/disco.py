#!/bin/python
import time
from sense_hat import SenseHat

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE =  (255,255,255)
COLORS = [RED, GREEN, BLUE, WHITE]

BLINKS = 10
INTERVAL = 0.1

sh = SenseHat()

color_index = 0

def get_color(index):
    return COLORS[index % len(COLORS)]

while True:
    color = get_color(color_index)
    for i in range(10):
        sh.clear(color)
        time.sleep(INTERVAL)
        sh.clear()
        time.sleep(INTERVAL)
    color_index += 1

