import re

import requests


class RenRen(object):
    def __init__(self):
        self.url = 'http://www.renren.com/972219026'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            'Cookie': "anonymid=k0ensl6v-ysfv9z; depovince=GW; _r01_=1; JSESSIONID=abcKxOgKTGsl4eiH8mE0w; ick_login=3ea5c01a-83ce-4a57-beca-4dcc8225d7e8; ick=3315965a-3bde-492a-a1b0-5e558524fa0f; t=1886a0927ee041d365f9c31564f4055e6; societyguester=1886a0927ee041d365f9c31564f4055e6; id=972219026; xnsid=e1cb788b; XNESSESSIONID=6599be7f2009; jebecookies=33f52e76-35bc-4619-8b49-ffc9ab419e31|||||; ver=7.0; loginfrom=null; jebe_key=8626ede3-db46-4cc7-bd0d-748df32c396b%7Cedd3323662e8fcb5593ebd4ca0a032eb%7C1568169888719%7C1%7C1568169887320; jebe_key=8626ede3-db46-4cc7-bd0d-748df32c396b%7Cedd3323662e8fcb5593ebd4ca0a032eb%7C1568169888719%7C1%7C1568169887323; wp_fold=0"
        }

    def request_post(self):
        response = requests.get(url=self.url, headers=self.headers)
        print(response.status_code)
        return response.content.decode()


if __name__ == '__main__':
    ren = RenRen()

    a = re.findall('关注内容', ren.request_post())
    print(a)
