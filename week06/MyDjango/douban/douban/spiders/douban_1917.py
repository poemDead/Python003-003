import scrapy
from douban.items import DoubanItem

class Douban1917Spider(scrapy.Spider):
    name = 'douban-1917'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/30252495/comments?status=P']

    def parse(self, response):  
        comments = response.xpath("//div[@id='comments']/div")
        for comment in comments:
            item = DoubanItem()
            item['good_num'] = comment.xpath(".//span[@class='votes vote-count']/text()").extract_first()
            item['star_num'] = comment.xpath(".//span[@class='allstar50 rating']/@title").extract_first()
            item['comment'] = comment.xpath(".//span[@class='short']/text()").extract_first()
            yield item
