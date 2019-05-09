

from robot import Robot		#robot is an installed package.
import motordriver
from AX12 import AX12
import gpio

from time import sleep
from threading import Thread
import math

from starting_block import manage_time_elapsed

#switch_pin_bcm    = gpio.gpio_index_of_wpi_pin    (22)
switch_pin_bcm = 6

gpio.set_pull_up_down(  switch_pin_bcm,     gpio.PULL_UP)
gpio.set_pin_mode(      switch_pin_bcm,     gpio.INPUT)

while 1:
    if gpio.digital_read(switch_pin_bcm) == 1:
        print("yes !")
