import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    req_content = req.read()

    with open(img_name, "wb") as f:
        f.write(req_content)

def main():

    gevent.joinall([gevent.spawn(downloader, "1.jpg", "http://img.alicdn.com/imgextra/i2/32109357/O1CN01Eudot12IzYYPvM3TZ_!!0-saturn_solar.jpg_220x220.jpg_.webp"), gevent.spawn(downloader, "2.jpg", "http://img.alicdn.com/imgextra/i2/24907328/O1CN01240Gpm1aJbhOWgm_!!0-saturn_solar.jpg_220x220.jpg_.webp")])

if __name__ == "__main__":
    main()