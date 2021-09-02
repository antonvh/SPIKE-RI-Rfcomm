#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from spikerfcomm import SpikePrimeREPL

SPIKE_BT_ADDR = 'F4:84:4C:C8:E0:47'
r = SpikePrimeREPL(SPIKE_BT_ADDR)
print("According to SPIKE, 1+1=", r.run("print(1+1)"))


# # Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

mb = Motor(Port.B)
mc = Motor(Port.C)

motors = [mb,mc]
for m in motors:
    m.reset_angle(0)
    # Default: 400, 1200, 5, 23, 5, 0 for kp, ki, kd, integral_range, integral_rate, feed_forward
    m.control.pid(40, 0, 0, 23, 5, 0)

r.run("from hub import port")


while not ev3.buttons.pressed():
    for m in motors:
        m.track_target(0)
    left = mb.angle()*3
    right = mc.angle()*-3
    r.run(
"""port.A.pwm({0})
port.B.pwm({1})""".format(left,right)
        )
    wait(25)

r.run(
"""port.A.pwm(0)
port.B.pwm(0)"""
        )








