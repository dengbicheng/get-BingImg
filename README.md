# Biying Spider

这是一个用于爬取必应每日壁纸网站（https://bing.ioliu.cn/）的爬虫程序。

## 功能

- 爬取必应每日壁纸网站的壁纸信息，包括图片链接、名称、上传时间和下载次数。
- 将壁纸信息存储到 `BiyingItem` 对象中。
- 使用管道将 `BiyingItem` 对象传递给后续处理程序。

## 依赖

- scrapy：用于编写和运行爬虫程序。
- ..items：包含用于存储爬取数据的 `BiyingItem` 对象。

## 使用方法

1. 安装所需的依赖库。
2. 创建一个新的 Scrapy 项目。
3. 在项目中创建一个名为 `BySpider` 的 Python 文件，并将上述代码复制到文件中。
4. 运行爬虫程序：`scrapy crawl by`。

## 代码说明

### 爬虫设置

- `name = 'by'`：爬虫的名称。
- `allowed_domains = ['bing.ioliu.cn']`：指定允许爬取的域名。
- `start_urls = ['https://bing.ioliu.cn/']`：起始 URL 列表。
- `b = 1`：用于控制爬取的页面数。
- `base_url = 'https://bing.ioliu.cn/?p='`：用于构建每个页面的 URL。

### 解析响应

- `parse(self, response)` 方法：用于解析爬取到的响应。
- 使用 XPath 表达式从响应中提取壁纸信息。
- 使用提取的信息创建一个 `BiyingItem` 对象，并通过 `yield` 将其传递给管道进行处理。

### 翻页爬取

- `if self.b <= 131`：控制爬取页面的数量，这里设置为最多爬取 131 页。
- `self.b = self.b + 1`：每爬取一页，计数器加一。
- `url = self.base_url + str(self.b)`：构建下一页的 URL。
- `yield scrapy.Request(url=url, callback=self.parse)`：发送请求，继续爬取下一页，并将响应交给 `parse` 方法处理。

以上是关于这个爬虫程序的说明文档，希望对你有所帮助！如有任何问题，请随时提问。    