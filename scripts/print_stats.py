#!/bin/python
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


def print_stats():
    print("humidity", sense.get_humidity())
    print("pressure", sense.get_pressure())
    print("temperature", sense.get_temperature())


if __name__ == "__main__":
    while True:
        print_stats()
        time.sleep(3)

