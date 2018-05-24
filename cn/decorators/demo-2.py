# 既不需要侵入，也不需要函数重复执行
import time


def deco(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        msecs = (end - start) * 1000
        print('time is {} ms'.format(msecs))

    return wrapper


@deco
def func():
    print('hello')
    time.sleep(1)
    print('world')


if __name__ == '__main__':
    func()
