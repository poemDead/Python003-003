# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class MaoyanPipeline(object):
    def __init__(self):
        self.f = open("movie.csv","a",encoding='utf-8',newline="")
        self.fieldnames = ["title","genre","date"]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):

        self.writer.writerow(item)
        return item

    def close(self,spider):
        self.f.close()
