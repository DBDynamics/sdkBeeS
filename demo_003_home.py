import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0

# 高级使能
# 软件限位 无效-0 有效-1
# 传感器限位 生效-0 无效-1
# 报警 释放电机-0 自动恢复-1
m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)

# 设置回零的速度
m.setTargetVelocity(mid, 200)
# 设置回零的方向
m.setHomingDirection(mid, -1)  # or -1
# 设置回零的触发电平 这个由传感器决定 常开的选0 长闭的选1 注意传感器选NPN类型的
m.setHomingLevel(mid, 0)  # or 1

# 切换到回零模式 开始回零操作
m.setHomingMode(mid)
print("开始回零....")

# 等待回零到位完成
m.waitTargetPositionReached(mid)
print("回零完成")


m.stop()
