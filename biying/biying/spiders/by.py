import scrapy
from ..items import BiyingItem

class BySpider(scrapy.Spider):
    name = 'by'
    allowed_domains = ['bing.ioliu.cn']
    start_urls = ['https://bing.ioliu.cn/']
    b = 1
    base_url = 'https://bing.ioliu.cn/?p='
    def parse(self, response):
        url = response.xpath('/html/body/div[@class="container"]/div[@class="item"]')

        for li in url:
            img_link = li.xpath('./div/div[@class="options"]/a[@class="ctrl download"]/@href').get()
            name = str(li.xpath('./div/div[@class="description"]/h3/text()').get())[1:6]#text()获取文本内容
            up_time = li.xpath('./div/div[@class="description"]/p[@class="calendar"]/em/text()').get()
            downloads = li.xpath('./div/div[@class="description"]/p[@class="view"]/em/text()').get()
            print(img_link)
            print(name)
            print(up_time)
            print(downloads)

            bookitem = BiyingItem(img_link=img_link,name=name,up_time=up_time,downloads=downloads)
            # 将bookitem对象传给管道
            yield bookitem
        if self.b <= 131:
            self.b = self.b + 1
            url = self.base_url + str(self.b)
            print('正在爬取：',url)
            yield scrapy.Request(url=url, callback=self.parse)  # 发送请求 指定函数处理

