import json

import requests


class douban(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=200&page_start=1'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        self.movielist = []

    def data_list(self):
        response = requests.get(url=self.url, headers=self.headers)
        restr = response.content.decode()
        redict = json.loads(restr)
        relist = redict['subjects']
        for movie in relist:
            temp = {}
            temp['title'] = movie['title']
            temp['rate'] = movie['rate']
            temp['id'] = movie['id']
            self.movielist.append(temp)

    def data_save(self):
        with open('movie.json', 'w', encoding='utf8') as f:
            json.dump(self.movielist, f, ensure_ascii=False)

    def run(self):
        self.data_list()
        self.data_save()


if __name__ == '__main__':
    movie = douban()
    movie.run()
