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