import time
import threading

def func():
    print("Start func")
    time.sleep(2)
    print("End func")

print("Main thrad")

t1 = threading.Thread(target=func, args=())
# 守护线程必须在子线程启动之前设置,否则无效.
t1.setDaemon(True)  # 这两个用法同样的效果
t1.daemon = True    # 设置守护线程后,子线程的最后语句print("End func")在主线程结束后不执行
t1.start()

time.sleep(1)
print("Main thread end")