# 带有不定参数的装饰器
import time


def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        msecs = (end - start) * 1000
        print('time is {} ms'.format(msecs))

    return wrapper


@deco
def func(a, b):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is {}'.format(a + b))


@deco
def func2(a, b, c):
    print('hello, here is a func for add: ')
    time.sleep(1)
    print('result is {}'.format(a + b + c))


if __name__ == '__main__':
    func(3, 4)
    func2(3, 4, 5)
