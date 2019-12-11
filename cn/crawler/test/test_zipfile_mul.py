import zipfile
import random
import time
import sys


class MyIterator(object):
    letters = 'abcdefghijklmnopqrstuvwxyz012345678'
    min_digits = 0
    max_digits = 0

    def __init__(self, min_digits, max_digits):
        if min_digits < max_digits:
            self.min_digits = min_digits
            self.max_digits = max_digits
        else:
            self.min_digits = max_digits
            self.max_digits = min_digits

    def __iter__(self):
        return self

    def __next__(self):
        rst = str()
        for item in range(0, random.randrange(self.min_digits, self.max_digits + 1)):
            rst += random.choice(self.letters)
        return rst


def extract():
    start_time = time.time()
    zfile = zipfile.ZipFile("d:/gz/test.zip")
    for p in MyIterator(5, 6):
        try:
            zfile.extractall(path='d:/gz/temp', pwd=str(p).encode('utf-8'))
            print("this password is {}".format(p))
            now_time = time.time()
            print("spend time is {}".format(now_time - start_time))
            sys.exit(0)
        except Exception as e:
            pass


if __name__ == '__main__':
    extract()
