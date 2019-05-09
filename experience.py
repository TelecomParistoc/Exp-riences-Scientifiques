

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

ax_shoot = AX12(121)
ax_shoot.move(100)
ax_pump = AX12(163)
ax_pump.move(-30)
ax_pump.set_speed(5)

turning_left = True

previous = gpio.digital_read(switch_pin_bcm)

while gpio.digital_read(switch_pin_bcm) == previous:
    sleep(1)
    
ax_shoot.move(130)

while True:
    if turning_left:
        ax_pump.move(30)
    else:
        ax_pump.move(-30)
    turning_left = not turning_left
    sleep(3)
