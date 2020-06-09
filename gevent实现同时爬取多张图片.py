import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

"""使用gevent实现多任务 同时在网上爬取两张图片"""

def downloader(img_name, img_url):
    #获取一个对象，该对象内存的是网址的源码
    req = urllib.request.urlopen(img_url)
    #将上一步获取的对象读出来，存到req_content变量里
    req_content = req.read()

    #将一个文件名以可写模式打开，然后将上一步读到的内容存在该文件里
    with open(img_name, "wb") as f:
        f.write(req_content)

def main():

    #通过gevent将任务放进去实现并发执行，并且传入相关的参数，图片名以及图片url
    gevent.joinall([gevent.spawn(downloader, "1.jpg", "http://img.alicdn.com/imgextra/i2/32109357/O1CN01Eudot12IzYYPvM3TZ_!!0-saturn_solar.jpg_220x220.jpg_.webp"), gevent.spawn(downloader, "2.jpg", "http://img.alicdn.com/imgextra/i2/24907328/O1CN01240Gpm1aJbhOWgm_!!0-saturn_solar.jpg_220x220.jpg_.webp")])

if __name__ == "__main__":
    main()