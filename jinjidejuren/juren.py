import random
import threading
import time

import requests
import re
import os


class juren(object):
    # 请输入绝对路径!
    def __init__(self, path):
        self.root = 'https://manhua.fzdm.com/39/'
        self.headers = {'Connection': 'close', "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        self.allbook = None
        self.path = path
        self.threadlist = []
        self.proxies_list = []
        self.picture_proxies_list = []
        self.count = 0
        self.lock = threading.Lock()

    # 创建ip代理池
    def ips(self):
        url = 'http://webapi.http.zhimacangku.com/getip?num=200&type=1&pro=&city=0&yys=0&port=1&pack=64043&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        response = requests.get(url, headers=self.headers)
        ip_list = response.text.split('\r\n')
        for ip in ip_list:
            ip_dict = {}
            ip_dict['http'] = ip
            print("加入ip代理池成功")
            self.proxies_list.append(ip_dict)
        # for proxies in self.proxies_list:
        #     try:
        #         requests.get('http://p0.manhuapan.com/2019/08/22151020345795.jpg', headers=self.headers, proxies=proxies)
        #     except:
        #         print(proxies, end='')
        #         print("测试此ip代理爬取图片失败")
        #     else:
        #         self.picture_proxies_list.append(proxies)
        #         print("此ip代理爬取图片可取")
        # print("可用图片代理个数为" + str(len(self.picture_proxies_list)))

    # 获取代理ip函数
    def get_ip(self, picture=False):
        if picture:
            return random.choice(self.picture_proxies_list)
        proxies = random.choice(self.proxies_list)
        flag = True
        while flag:
            try:
                requests.get('https://www.baidu.com', headers=self.headers)
            except:
                proxies = random.choice(self.proxies_list)
            else:
                flag = False
        return proxies

    # 获取漫画全部章节
    def book(self):

        html = requests.get(self.root, headers=self.headers).content.decode()
        self.allbook = re.findall('<li class="pure-u-1-2 pure-u-lg-1-4"><a href="(.*?)" title="(.*?)">', html)

    # 线程函数-爬取图片入口，循环内容单独写在一个函数中，发生异常重新执行
    def thread(self, path, book):
        for i in range(0, 100):
            print("thread")
            flag = True
            over = False
            while flag:
                try:
                    if not self.again(i, path, book):
                        over = True
                        break
                except:
                    print("爬取" + path + "\033[31m发生异常!!!!!!!!\033[0m")
                else:
                    flag = False
            if over == True:
                break
        self.lock.acquire()
        self.count += 1
        print('\033[34m此章节爬取完毕此章节爬取完毕此章节爬取完毕此章节爬取完毕此章节爬取完毕此章节爬取完毕此章节爬取完毕\033[0m' + str(self.count))
        self.lock.release()
            # url = self.root + "/" + book[0] + "/index_" + str(i) + ".html"
            # print(url)
            # html = requests.get(url, headers=self.headers).text
            # if html == '404':
            #     break
            # result = re.findall('var mhurl="(.*?)";', html)
            # result = result[0]
            # imgurl = 'http://p0.manhuapan.com/' + result
            # response = requests.get(imgurl, headers=self.headers)
            # file_name = path + "\\" + str(i) + ".jpg"
            # with open(file_name, 'wb') as f:
            #     f.write(response.content)
            # print(file_name + "successful")
            # time.sleep(2)

    # 线程函数-爬取图片执行函数，循环内容单独写在一个函数中，发生异常重新执行
    def again(self, i, path, book):
        url = self.root + "/" + book[0] + "/index_" + str(i) + ".html"
        print(url)
        html = requests.get(url, headers=self.headers, timeout=3).text
        if html == '404':
            file_name = self.path + "\\" + "进击的巨人\\AAA.txt"
            with open(file_name, 'a+') as f:
                f.write(str(book[1])+"章节下载完成")
            print('404')
            return False
        result = re.findall('var mhurl="(.*?)";', html)
        result = result[0]
        imgurl = 'http://p0.manhuapan.com/' + result
        response = requests.get(imgurl, headers=self.headers, timeout=3)
        file_name = path + "\\" + str(i) + ".jpg"
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(file_name + "\033[32msuccessful~~~~~~~~~~~~~~\033[0m")
        time.sleep(1)
        return True

    # 开始爬取函数
    def spider(self):
        # temp = 0
        # while True:
        #     flag = True
        #     temp10 = temp + 10
        #     if temp > len(self.allbook):
        #         break
        #     if temp10 > len(self.allbook):
        #         temp10 = len(self.allbook)
        #         flag = False
        #     #     每次开启十个线程爬取十个章节
            for book in self.allbook:
                print("sprider")
                path = self.path + "\\" + "进击的巨人\\" + book[1]
                os.makedirs(path)
                th = threading.Thread(target=self.thread, args=(path, book))
                self.threadlist.append(th)
                th.start()
            for i in self.threadlist:
                print(i)
                i.join()
                print("第" + str(i) + "号线程已结束")
            print("进程全部结束")
            # temp += 10
            # print("spiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderokspiderok")
            # if not flag:
            #     break
            print("整本书爬取完毕")
            # for i in range(0, 100):
            #     url = self.root + "/" + book[0] + "/index_" + str(i) + ".html"
            #     print(url)
            #     html = requests.get(url, headers=self.headers).text
            #     if html == '404':
            #         break
            #     result = re.findall('var mhurl="(.*?)";', html)
            #     result = result[0]
            #     imgurl = 'http://p0.manhuapan.com/' + result
            #     response = requests.get(imgurl)
            #     file_name = path + "\\" + str(i) + ".jpg"
            #     with open(file_name, 'wb') as f:
            #         f.write(response.content)
            #     print(file_name + "successful")
            #     time.sleep(2)

    # 程序执行入口
    def run(self):
        self.book()
        self.spider()



if __name__ == '__main__':
    j = juren("D:\PycharmProjects\spider\jinjidejuren")
    j.run()
