import json

import requests

class JinSan:

    def __init__(self, word):
        self.word = word
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        self.post = {'f': 'auto', 't': 'auto', 'w': self.word}

    def request_post(self):
        # 发送post请求，参数url， headers浏览器头部， data
        response = requests.post(url=self.url, headers=self.headers, data=self.post)
        return response.json()

    def parse_data(self, data):
        try:
            content = (data['content']['out'])
        except:
            content = None
            print("发生错误")
        print(content)

    def run(self):
        data = self.request_post()
        self.parse_data(data=data)


if __name__ == '__main__':
    while True:
        x = input("请输入汉语")
        fanyi = JinSan(x)
        fanyi.run()

