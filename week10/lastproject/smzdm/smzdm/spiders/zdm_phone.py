from time import sleep

import scrapy
import pandas as pd
import numpy as np
from snownlp import SnowNLP


class ZdmPhoneSpider(scrapy.Spider):
    name = 'zdm_phone'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/']

    def start_requests(self, ):
        start_urls = 'https://www.smzdm.com/fenlei/zhinengshouji/h4c4s0f0t0p1/#feed-main/' #
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        top10_info=[]
        for num in range(1,11):
            rank_xpath = f'//*[@id="feed-main-list"]/li[{num}]/@data-position'
            href_xpath = f'//*[@id="feed-main-list"]/li[{num}]/div/div[2]/h5/a/@href'
            title_xpath = f'//*[@id="feed-main-list"]/li[{num}]/div/div[2]/h5/a/text()'
            rank = response.xpath(rank_xpath).get()
            href = response.xpath(href_xpath).get()
            title = response.xpath(title_xpath).get()
            info = [rank,href,title]
            top10_info.append(info)
        for phone in top10_info:
            phone_rank = phone[0]
            phone_href = phone[1]
            phone_title = phone[2]
            sleep(2)
            yield scrapy.Request(
                url=phone_href,
                meta={'rank':phone_rank,'href':phone_href,'title':phone_title},
                callback=self.parse2)
    
    def parse2(self, response):
        rank = response.meta['rank']
        href = response.meta['href']
        title = response.meta['title']
        navi = response.xpath('//*[@id="comment"]/div[1]/ul[2]/li/a/text()')
        if navi:
            comment_pages = response.xpath('//*[@id="comment"]/div[1]/ul[2]/li/a/text()').extract()[:-1]
            for page in comment_pages:
                comment_url = href + f"p{page}"
                yield scrapy.Request(
                    url=comment_url,
                    meta={'rank':rank,'href':href,'title':title},
                    callback=self.parse3)
        else:
            temp = response.xpath('(//*[@id="commentTabBlockNew"]/ul/li/div[2]/div[@class="comment_conWrap"]/div[1]/p/span/text())').extract()
            temp = [i.strip() for i in temp]
            comments = [i for i in temp if i != '']
            comments_sen = [SnowNLP(i).sentiments for i in comments]
            for i in range(len(comments)):
                yield {
                    'rank': rank,
                    'href': href,
                    'title': title,
                    'comment': comments[i],
                    'comment_sen': comments_sen[i],
                }

    
    def parse3(self, response):
        rank = response.meta['rank']
        href = response.meta['href']
        title = response.meta['title']
        temp = response.xpath('(//*[@id="commentTabBlockNew"]/ul/li/div[2]/div[@class="comment_conWrap"]/div[1]/p/span/text())').extract()
        temp = [i.strip() for i in temp]
        comments = [i for i in temp if i != '']
        comments_sen = [SnowNLP(i).sentiments for i in comments]
        for i in range(len(comments)):
            yield {
                'rank': rank,
                'href': href,
                'title': title,
                'comment': comments[i],
                'comment_sen': comments_sen[i],
            }

