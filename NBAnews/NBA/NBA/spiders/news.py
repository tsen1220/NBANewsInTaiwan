import scrapy
import re
import sqlite3
import os


# ITEM
from NBA.items import NbaItem


# 時間處理
def timeStrHandle(time):
    time = "".join(time.split('-'))
    time = "".join(time.split(':'))
    time = "".join(time.split(' '))
    return time

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
        time = timeStrHandle(time[0])
        print(
            '----------------------------------------------------------------------------')

        # 確認資料庫有無資料
        BASE_DIR = os.path.dirname(os.path.dirname(
            os.path.abspath('././NBAnews/')))
        print(BASE_DIR)
        conn = sqlite3.connect(
            os.path.join(BASE_DIR, 'db.sqlite3'))
        c = conn.cursor()
        c.execute('SELECT title FROM main_imgnews WHERE time=%s' % time)
        data = c.fetchall()

        try:
            if(data != []):
                print('This data is existed!!')
            else:
                # 將資料寫入ITEM
                item['title'] = title[0]
                item['content'] = content
                item['time'] = time
                item['img'] = img[0]
                yield item
        except Exception as err:
            print(err)
