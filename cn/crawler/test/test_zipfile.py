import zipfile
import time
import threading

startTime = time.time()
flag = True


def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='d:/gz/temp', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        global flag
        flag = False
        print("耗时：{}".format(nowTime - startTime))
    except Exception as e:
        pass


def do_main():
    zfile = zipfile.ZipFile("d:/gz/test.zip", 'r')
    for number in range(1, 9999):
        if flag is True:
            t = threading.Thread(target=extract, args=(number, zfile))
            t.start()
            t.join()


if __name__ == '__main__':
    do_main()
