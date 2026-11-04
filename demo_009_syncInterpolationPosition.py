import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')

# 高级使能
# 软件限位 无效-0 有效-1
# 传感器限位 生效-0 无效-1
# 报警 释放电机-0 自动恢复-1
for mid in range(0, 8):
    m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)

# 设置为同步插补位置模式
for mid in range(0, 8):
    m.setInterpolationPositionMode(mid)

# 获取当前位置
for mid in range(0, 8):
    m._last_si_pos[mid] = m.getActualPosition(mid)

# 开始插补轨迹 dt 单位10ms, dt=100即100x10ms=1s pos为0-7轴的关键帧位置
m.setSIPose(dt=100, pos=[51200, 51200, 51200, 51200, 51200, 51200, 51200, 51200])
# 开始插补轨迹 dt 单位10ms, dt=100即100x10ms=1s pos为0-7轴的关键帧位置
m.setSIPose(dt=100, pos=[0, 0, 0, 0, 0, 0, 0, 0])
# 等待插补轨迹运行完成
m.waitSIP()

m.stop()
