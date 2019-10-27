import scrapy
import re
#
from NBA.items import NbaItem


# 爬蟲
class Nba(scrapy.Spider):
    # scrapy crawl {name}
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    # crawl urls(req)
    start_urls = [
        'https://nba.udn.com/nba/cate/6754/-1/newest/{}'.format(i) for i in range(1, 5)]

    def parse(self, response):
        # xpath
        url_list = response.xpath(
            '//div[@class="box_body"]/dl/dt/a/@href').extract()

        new_list = []

        for url in url_list:
            if('story' in url):
                new_list.append('http://nba.udn.com'+str(url))

        for url in new_list:

            # scrapy.Request crawl detail content      url=> request url   callback=> parse_detail callbackfunction
            yield scrapy.Request(url=url, callback=self.parse_content)

    def parse_content(self, response):
        item = NbaItem()

        title = response.xpath(
            '//h1[@class="story_art_title"]/text()').extract()
        content = response.xpath(
            '//p/text()').extract()
        content = ''.join(content)
        time = response.xpath(
            '//div [@class="shareBar__info"]/div[@class="shareBar__info--author"]/span/text()').extract()
        img = response.xpath(
            '//div[@id="story_body_content"]/span/p/figure/a/img/@data-src'
        ).extract()
        print(
            '----------------------------------------------------------------------------')

        item['title'] = title[0]
        item['content'] = content
        item['time'] = time[0]
        item['img'] = img[0]
        yield item
