import random
import time

from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
axis_num = 5
for axis in range(axis_num):
    m.setPowerOnPro(id=axis, limit_soft=0, limit_off=0, auto_recovery=0)
    m.setHomingLevel(axis, 0)
    m.setHomingDirection(axis, -1)
    m.setHomingTriggerLevel(axis, 400)
    m.setTargetVelocity(axis, 200)
    m.setHomingMode(axis)

for axis in range(axis_num):
    m.waitTargetPositionReached(axis)
    print("home done:", axis)

for axis in range(0, axis_num):
    m.setPowerOnPro(id=axis, limit_soft=0, limit_off=0, auto_recovery=0)
    m.setAccTime(axis, 300)
    m.setTargetVelocity(axis, 9000)

k = 51200 / 40.0
for loop in range(0, 3):
    for axis in range(0, axis_num):
        m.setTargetPosition(axis, 455 * k)
    for axis in range(0, 1):
        m.waitTargetPositionReached(axis)
    for axis in range(0, axis_num):
        m.setTargetPosition(axis, 5 * k)
    for axis in range(0, 1):
        m.waitTargetPositionReached(axis)

m.stop()
