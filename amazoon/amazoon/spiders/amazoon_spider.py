# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazoonItem

class AmazoonSpiderSpider(scrapy.Spider):
    name = 'amazoon_spider'
    start_urls = [
    				'https://www.amazon.com/s?k=gtx+1650&i=electronics&ref=nb_sb_noss'
    			]

    def parse(self, response):
        items = AmazoonItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-link-normal.a-text-bold').css('::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items