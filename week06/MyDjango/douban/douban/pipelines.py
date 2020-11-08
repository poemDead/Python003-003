# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DoubanPipeline:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='password',
            db='testdb',
            charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
            "INSERT INTO douban1917 (comment, star, vote) VALUES(%s, %s, %s)",
            (item['comment'],item['star_num'],item['good_num']))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f'Insert item failed {e}')
        return item
    
    def close_spider(self, spider):
        self.connection.close()
    
