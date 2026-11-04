import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0

m.setPositionMode(mid)
m.setEncoderPolarityP(mid)
m.setTargetVelocity(mid, 2000)
m.setAccTime(mid, 200)
m.setHomingLevel(mid,0)
m.setHomingDirection(mid, 1)
m.setPhaseCorrectCurrent(mid, 1500)
m.setKPP(mid, 30)
m.setKFF(mid, 10)
m.setKVF(mid, 15)
m.setPowerLimit(mid, 1500)
m.setEStopDec(mid, 500)


m.stop()
