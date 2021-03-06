# threading.currentThread(): 返回当前的线程变量
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
# 线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# run(): 用以表示线程活动的方法
# start():启动线程活动
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
# isAlive(): 返回线程是否活动的
# getName(): 返回线程名
# setName(): 设置线程名

# 可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法


import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        # 获取锁，用于此线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{0}: {1}".format(threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
