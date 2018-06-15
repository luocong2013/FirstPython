# 带有参数的装饰器
import time


def deco(func):
    def wrapper(a, b):
        start = time.time()
        func(a, b)
        end = time.time()
        msecs = (end - start) * 1000
        print('time is {} ms'.format(msecs))

    return wrapper


@deco
def func(a, b):
    print('hello, here is a func for add: ')
    time.sleep(1.5)
    print('result is {}'.format(a + b))


if __name__ == '__main__':
    func(3, 4)
