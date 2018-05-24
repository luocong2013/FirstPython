# 多个装饰器
import time


def deco01(func):
    def wrapper(*args, **kwargs):
        print('this is deco01')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        msecs = (end - start) * 1000
        print('time is {} ms'.format(msecs))
        print('deco01 end here')

    return wrapper


def deco02(func):
    def wrapper(*args, **kwargs):
        print('this is deco02')
        func(*args, **kwargs)
        print('deco02 end here')

    return wrapper


@deco01
@deco02
def func(a, b):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is {}'.format(a + b))


if __name__ == '__main__':
    func(3, 4)
