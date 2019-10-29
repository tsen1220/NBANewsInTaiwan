# 目錄

[啟動](#啟動)

[簡介](#簡介)

[爬蟲](#爬蟲)

[DjangoServer](#DjangoServer)

[登入](#登入)

[註冊](#註冊)

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
$ Scripts/activate
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

class Nba(scrapy.Spider):
    # scrapy crawl
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = [req.url ]

    # then parse the request
      def parse(self, response):

```

排程部分基本上就是在執行緒中設定無窮的 callback，並設定執行緒的睡眠時間。

而為了避免爬取以存取的資料，會先使用 SQL 語法確認資料庫是否有存放過的資料，在這我是用時間以及標題去判斷。

```

sql=SELECT title FROM main_imgnews WHERE time=%s' % time

```

#DjangoServer

使用 Django 架設後端伺服器，爬蟲完的資料會經由 Scrapy 的 pipeline 將 item 進行處理，並將其送至我們設定的位置，在這裡是由 Django model 去接收，使用 SQLite 存取。

接下來會將資料製作成 RESTful API ，使用 Django 的 rest Framework。

<img>
