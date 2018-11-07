"""
使用threading模块实现一个新的线程，需要下面3步：

定义一个 Thread 类的子类
覆盖 __init__(self [,args]) 方法，可以添加额外的参数
最后，需要覆盖 run(self, [,args]) 方法来实现线程要做的事情
当你创建了新的 Thread 子类的时候，你可以实例化这个类，调用 start() 方法来启动它。线程启动之后将会执行 run() 方法
"""

import threading
import _thread
import time

exitFlag = 0


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("starting" + self.name)
        print_time(self.name, self.counter, 3)
        print("exiting" + self.name)


# Create new threads
thread1 = myThread(1, 'Thread_1', 1)
thread2 = myThread(2, 'Thread_2', 2)

# start new threads
thread1.start()
thread2.start()

# join() 命令控制主线程的终止
thread1.join()
thread2.join()
print("Exiting Main Thread")
