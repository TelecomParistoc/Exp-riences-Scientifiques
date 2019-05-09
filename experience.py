

from robot import Robot		#robot is an installed package.
import motordriver
from AX12 import AX12
import gpio

from time import sleep
from threading import Thread
from random import random
import math

from starting_block import manage_time_elapsed

gpio.init()

#switch_pin_bcm    = gpio.gpio_index_of_wpi_pin    (22)
switch_pin_bcm = 6

gpio.set_pull_up_down(  switch_pin_bcm,     gpio.PULL_UP)
gpio.set_pin_mode(      switch_pin_bcm,     gpio.INPUT)

ax = AX12(121)
ax.move(100)

previous = gpio.digital_read(switch_pin_bcm)
while 1:
    sleep(random()*2)
    if gpio.digital_read(switch_pin_bcm) != previous:
        if previous :
            ax.move(130)
        else:
            ax.move(100)
        previous = 1-previous
