import scrapy

from ..items import CnblogItem


class Cnblog_Spider(scrapy.Spider):
    # 名字 名字必须唯一
    name = "cnblog"
    # 约束此爬虫不可以爬出此域名外网站
    allowed_domains = ['cnblogs.com']
    # 爬取的url队列
    start_urls = [
        'https://www.cnblogs.com/'
    ]

    # 运转之后，请求地址之后会回调parse方法，并将返回的页面当作参数
    def parse(self, response):
        item = CnblogItem()
        item['title'] = response.xpath('//a[@class="titlelnk"]/text()').extract()
        item['url'] = response.xpath('//a[@class="titlelnk"]/@href').extract()
        # 写yield会将item送入管道函数中 pipelines
        yield item
