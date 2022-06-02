# -*- coding: utf-8 -*-
"""
Created on Sun May 29 23:32:20 2022

@author: amuralles
"""

import scrapy
from imdb.items import ImdbItem
import os

class Review(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"]
    custom_settings = {'FEEDS': {'file:'+os.getcwd()+'/imdb_most_popular_reviews.csv':{'format': 'csv','overwrite':True}}}
    def parse(self, response):
        urls = []
        href_lst=response.css('td.titleColumn a').xpath('@href').getall()
        for href in href_lst[0:25]:
            href=href.split('?')[0]
            url=response.urljoin(href)+'reviews/_ajax'
            if url not in urls:
                urls.append(url)
                yield scrapy.Request(url, callback=self.parse_reviews)

    def parse_reviews(self,response):
        
        content_lst=response.css('div.lister-item-content')
        for content in content_lst:
            yield ImdbItem( 
                rating=content.css('span.rating-other-user-rating span::text').get(),
                review=''.join(content.css('div.text.show-more__control::text').getall())
                )

        
        pagKey=response.css('div.load-more-data').xpath('@data-key').get()    
        if pagKey:
            next_page=response.urljoin('?paginationKey='+str(pagKey))
            yield scrapy.Request(next_page, callback=self.parse_reviews)
            
        