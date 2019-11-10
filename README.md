# Catalog/目錄

## English

[GettingStarted](#GettingStarted)

[Crawl](#Crawl)

[Django](#Django)

[React](#React)

## 中文

[啟動](#啟動)

[簡介](#簡介)

[爬蟲](#爬蟲)

[DjangoServer](#DjangoServer)

[ReactFramework](#ReactFramework)

如果你喜歡，請給我一顆星，我會很感謝你。

If you like this, please give me a star. Thank you!!

# GettingStarted

## Run server

Hello, you can start this project by installing React and others modules with front-end by npm.

```
$ npm install
```

Run the react Server.

```
npm start
```

Back-end is Developed by django. We need to create virtual environment.

```
$ cd env
$ Scripts/activate (Windows)
$ source bin/activate (MacOS/Linux)
```

Then, install the modules we require.

```
$ pip install -r requirement.txt
```

In the end, run the back-end server.

```
$ py manage.py runserver
```

<br />
<hr />
Hint: The info below is how to create new django project.

When requirement.txt installing is finished, create the django project and app.

```
$ django-admin startproject yourprojectname
```

You need to change directory to your project name and then create the app.

Please remember your django setting.

```
$ django-admin startapp yourappname
```

<hr />

## Introduction

This website crawls the NBA news in Taiwan via Scrapy.

I loop the scrapy to get news every 100 seconds

Back-end processes the data in the Django Model (ORM) , inserts it into SQLite3, designs the RESTful API for news.

Front-end presents news by React and React Routers.

Highlight:

<img src='https://raw.githubusercontent.com/tsen1220/NBANewsInTaiwan/master/img/highlight.jpg' alt=''>

News list:

<img src='https://raw.githubusercontent.com/tsen1220/NBANewsInTaiwan/master/img/list.jpg' alt=''>

# Crawl

I use the scrapy to crawl the news.

The spider settings:

```
crawl setting:

class Nba(scrapy.Spider):
    # scrapy crawl
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = [req.url ]

    # then parse the request
      def parse(self, response):
    ....
    ....
    yield scrapy.Request(url=the new url, callback=self.parse_content)

    def parse_content(self,response):
    ....
    ....

```

This is the scrapy endless loop settings.

```
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from twisted.internet.task import deferLater

def sleep(self, *args, seconds):
    return deferLater(reactor, seconds, lambda: None)


process = CrawlerProcess(get_project_settings())

def _crawl(result, spider):

    deferred = process.crawl(spider)
    deferred.addCallback(lambda result: print(
        'waiting yoursetting  before restart'))
    deferred.addCallback(sleep, setting sleep seconds )
    deferred.addCallback(_crawl, spider)
    return deferred


_crawl(None, Nba)
process.start()

```

When all settings are ok, crawl the news.

```

scrapy crawl yourspidername

```

I use SQL to check the crawling news which is existed in database by time and title.

```

sql=SELECT title FROM main_imgnews WHERE time=%s' % time

```

# Django

Django handles the item from scrapy pipeline, inserts these into SQLite3 by Django Model.

Then designs the RESTful API for data.

<img src='https://raw.githubusercontent.com/tsen1220/NBANewsInTaiwan/master/img/api.jpg' alt=''>

```
API setting:

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = imgnews
        fields = ('id', 'title', 'content', 'time', 'img')

```

Scrapy_DjangoItem setting:

```
Scrapy settings:


import django

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'NBAnews.settings'
django.setup()


item:

from scrapy_djangoitem import DjangoItem


from main.models import imgnews


class NbaItem(DjangoItem):
    django_model = imgnews
```

# React

Use react with components to present the NBA news in Taiwan.

Router settings:

```
    <Route exact path="/" component={Home} />
    <Route exact path="/news" component={ArticleList} />
    <Route exact path="/news/:articleID" component={ArticleDetail} />

```

# 啟動

## 前端

React。

請先安裝 Node 與 Npm。

並輸入下面的指令安裝 modules。

```
$ npm install
```

啟動伺服器

```
$ npm start
```

預設 Port 為 3000，位於 localhost。

## 後端

Python Django 開發。

須先進入虛擬環境。

```
$ cd env
$ Scripts/activate (Windows)
$ source bin/activate (MacOS/Linux)
```

成功進入虛擬環境後進入 src 目錄，並安裝所需 modules。

```
$ pip install -r requirement.txt
```

安裝完成後，啟動伺服器 Server。

```
$ py manage.py runserver
```

# 簡介

這網站是經由 Scrapy 框架執行網路爬蟲，將 NBA 相關新聞爬取下來，由 Django Model 處理資料，並放入資料庫，將新聞製作成 Restful API，由前端 React 呈現。

主要分工為爬蟲、後端伺服器資料處理以及 API 製作，資料庫儲存，React 使用 Ajax 請求資料並 Router 呈現不同的報導。

有設定網路的爬蟲排程，所以會持續更新資料以及 API，為使用者提供最新的資訊。

焦點新聞:

<img src='https://raw.githubusercontent.com/tsen1220/NBANewsInTaiwan/master/img/highlight.jpg' alt=''>

新聞列表:

<img src='https://raw.githubusercontent.com/tsen1220/NBANewsInTaiwan/master/img/list.jpg' alt=''>

# 爬蟲

爬蟲細節就不多談，基本上就是散佈 spider 設定 request 的網址並解析:

```
crawl setting:

class Nba(scrapy.Spider):
    # scrapy crawl
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = [req.url ]

    # then parse the request
      def parse(self, response):
    ....
    ....
    yield scrapy.Request(url=the new url, callback=self.parse_content)

    def parse_content(self,response):
    ....
    ....

```

排程部分基本上就是在執行緒中設定無窮的 callback，並設定執行緒的睡眠時間。

```
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from twisted.internet.task import deferLater

def sleep(self, *args, seconds):
    return deferLater(reactor, seconds, lambda: None)


process = CrawlerProcess(get_project_settings())

def _crawl(result, spider):

    deferred = process.crawl(spider)
    deferred.addCallback(lambda result: print(
        'waiting yoursetting  before restart'))
    deferred.addCallback(sleep, setting sleep seconds )
    deferred.addCallback(_crawl, spider)
    return deferred


_crawl(None, Nba)
process.start()

```

之後執行指令即可爬蟲。

```

scrapy crawl yourspidername

```

而為了避免爬取已存取的資料，會先使用 SQL 語法確認資料庫是否有存放過的資料，在這我是用時間以及標題去判斷。

```

sql=SELECT title FROM main_imgnews WHERE time=%s' % time

```

# DjangoServer

使用 Django 架設後端伺服器，爬蟲完的資料會經由 Scrapy 的 pipeline 將 item 進行處理，並將其送至我們設定的位置，在這裡是由 Django model 去接收，使用 SQLite 存取。

接下來會將資料製作成 RESTful API ，使用 Django 的 rest Framework。

<img src='https://raw.githubusercontent.com/tsen1220/NBANewsInTaiwan/master/img/api.jpg' alt=''>

```
API setting:

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = imgnews
        fields = ('id', 'title', 'content', 'time', 'img')

```

DjangoItem 設定好才能經由 pipeline 將資料送入 Django。

```
Scrapy settings:


import django

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'NBAnews.settings'
django.setup()


item:

from scrapy_djangoitem import DjangoItem


from main.models import imgnews


class NbaItem(DjangoItem):
    django_model = imgnews
```

# ReactFramework

最後我是用 React 來將頁面呈現，寫了相關的 component，使用 props 來進行資料的呈現。

採用 react-router-dom 來做這頁面的 Router，並製成 SPA 介面。

Router 設定為:

```
    <Route exact path="/" component={Home} />
    <Route exact path="/news" component={ArticleList} />
    <Route exact path="/news/:articleID" component={ArticleDetail} />

```
