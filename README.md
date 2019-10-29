# 目錄

[啟動](#啟動)

[簡介](#簡介)

[新話題](#新話題)

[留言](#留言)

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

由於有設定網路的爬蟲排程，所以會持續更新資料以及 API，為使用者提供最新的資訊。

<img src='https://raw.githubusercontent.com/tsen1220/DjangoReact-Forum/master/intro/Home.jpg' alt=''>
