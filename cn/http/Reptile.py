import urllib
import urllib.request
import re


def download_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html))  # repr用来转换表达式类型字符串
    num = 1
    for img in get_img:
        image = download_page(img)
        with open('%s.jpg' % num, 'wb') as fp:
            fp.write(image)
            num += 1
            print("正在下载第%s张图片" % num)
    return


url = 'http://tieba.baidu.com/p/5513894858'
html = download_page(url)
get_image(html)
