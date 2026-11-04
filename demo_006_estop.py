import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0

# 设置急停模式减速系数 数值越大 减速度越大 减速时间越小
# 数值以实际测试为准 默认500 推荐范围 100 - 2000 负载质量大的 应选数值小一些
m.setEStopDec(mid, 500)

# 无论速度模式 位置模式 或者 回零模式 调用改指令 都会切换到急停模式 完全停止后会自动切换为位置模式
# 急停过程的减速度可以通过急停减速系数进行设置
m.setEStopMode(mid)

m.stop()
