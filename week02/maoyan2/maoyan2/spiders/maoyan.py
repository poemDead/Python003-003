import scrapy
from scrapy import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    #allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        print('yes')
        for movie in movies:
            yield {
                'title': movie.xpath('./div[1]/span/text()').get(),
                'genre': movie.xpath('./div[2]/text()')[1].get().strip(),
                'date': movie.xpath('./div[4]/text()')[1].get().strip()
            }

