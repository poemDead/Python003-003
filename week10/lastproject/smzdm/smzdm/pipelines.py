# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class SmzdmPipeline:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='password',
            db='zdmdb',
            charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
            "INSERT INTO zdm_phone (comment_rank, comment_href, comment_title, comment_cotents, comment_sen ) VALUES(%s, %s, %s, %s,%s)",
            (item['rank'],item['href'],item['title'],item['content'],item['sen']))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f'Insert item failed {e}')
        return item
    
    def close_spider(self, spider):
        self.connection.close()



    
