# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request

class BiyingPipeline:
    def process_item(self, item, spider):
        return item

class PhotoPipeline:
    def process_item(self,item,spider):
        #urlretrieve()方法直接将远程数据下载到本地
        #url      需要下载的链接
        #filename 保存在本地的路径
        URL=item.get('img_link')
        FileName=r'C:\Users\19456\Pictures\素材\风景图片\\'+str(item.get('name'))+'.jpg'
        urllib.request.urlretrieve(url=URL,filename=FileName)
        return item


class DownloadPipeline(FilesPipeline):
    #def process_item(self,item,sider):
    def get_media_requests(self, item, info):
        url = item.get('img_link')
        name = item.get('name')
        # 依次对图片地址发送请求，meta用于传递图片的文件名
        yield scrapy.Request(url=url, meta={'name':name+'.jpg'})

    def file_path(self, request, response=None, info=None, *, item=None):

        filename = request.meta['name']
        return filename

    def item_completed(self, results, item, info):
        print('正在下载：',item.get('name'))
        return item



import pymysql

class MysqlPipeline:
    # 连接数据库
    def open_spider(self, spider):
        print('=======open_spider=======')
        # 获取settings属性
        host = spider.settings.get('DB_HOST')  # 主机
        port = spider.settings.get('DB_PORT')  # 端口号
        user = spider.settings.get('DB_USER')  # 用户名
        password = spider.settings.get('DB_PASSWORD')  # 密码
        db = spider.settings.get('DB_NAME')  # 数据库名
        charset = spider.settings.get('DB_CHARSET')  # 字符编码
        # 连接数据库
        self.connect = pymysql.connect(
            host=host, port=port, user=user, password=password, db=db, charset=charset
        )
        self.cursor = self.connect.cursor()


    # 数据库写入数据
    def process_item(self, item, spider):
        sql = 'INSERT INTO biying_images (img_name, img_link, img_uptime, downloads) values (%s,%s,%s,%s)'
        values = (item.get('name'),item.get('img_link'),item.get('up_time'),item.get('downloads'))

        try:
            self.cursor.execute(sql, values)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            # 处理异常，如打印错误日志等
            print("An error occurred during database insertion:", e)

        return item

    # 关闭连接
    def close_spider(self, spider):
        print('=======close_spider=======')
        try:
            self.cursor.close()
            self.connect.close()
        except Exception as e:
            # 处理异常，如打印错误日志等
            print("An error occurred during closing the database connection:", e)
