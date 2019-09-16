# 爬取校花吧图片
import requests
from lxml import etree
import os

class Baidu:
    def __init__(self, name):
        self.url = 'http://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
        # 使用不支持js的浏览器请求头
        self.headers = {
            'Connection': 'close',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) '
            }

    def get_page(self):
        req = requests.get(self.url, headers=self.headers)
        return req.content.decode()

    def parse_url_list(self, data):
        html = etree.HTML(data)
        node_list = html.xpath("//ul[@id='thread_list']//a[@class='j_th_tit ']/@href")
        print(node_list)
        for i in range(len(node_list)):
            node_list[i] = 'http://tieba.baidu.com' + node_list[i]
        return node_list

    def get_image(self, url_list):
        os.mkdir(os.path.join(os.path.dirname(__file__), str('/校花/')))
        for page in url_list:
            result = requests.get(page, headers=self.headers)
            html = etree.HTML(result.content.decode())
            print(result.content.decode())
            img_url = html.xpath("//cc//img[@class='BDE_Image']/@src")
            print(img_url)
            self.download(img_url)

    def download(self, img_url):
        for img in img_url:
            result = requests.get(img, headers=self.headers)
            name = str(img).split('/')
            name = os.path.join(os.path.dirname(__file__), str('/校花/' + name[-1]))

            with open(name, 'wb') as f:
                f.write(result.content)


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    baidu = Baidu('校花吧')
    result = baidu.get_page()
    url_list = baidu.parse_url_list(result)
    baidu.get_image(url_list)
