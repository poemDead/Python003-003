# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class Maoyan10Spider(scrapy.Spider):
    name = 'maoyan10'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?sortId=3']
    
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movies:
            yield {
                'title': movie.xpath('./div[1]/span/text()').get(),
                'genre': movie.xpath('./div[2]/text()')[1].get().strip(),
                'date': movie.xpath('./div[4]/text()')[1].get().strip()
            }
