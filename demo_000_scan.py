from DBDynamics import BeeS
# for windows, m = Bee('com3')
m = BeeS('/dev/ttyUSB0')
m.scanDevices()
m.stop()
