# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazoonItem

class AmazoonSpiderSpider(scrapy.Spider):
    name = 'amazoon_spider'
    start_urls = [
    				'https://www.amazon.com/ZOTAC-GeForce-128-Bit-Graphics-ZT-T16500F-10L/dp/B07QF1H9YR/ref=sxin_0_ac_d_rm?ac_md=0-0-Z3R4IDE2NTA%3D-ac_d_rm&cv_ct_cx=gtx+1650&dchild=1&keywords=gtx+1650&pd_rd_i=B07QF1H9YR&pd_rd_r=e02dc07c-ba53-4b0f-b567-079c046a49b4&pd_rd_w=UA9qw&pd_rd_wg=IZlq2&pf_rd_p=ec111f65-4a46-499c-be78-f47997212bd0&pf_rd_r=DAVQRP12X837VEDJWBVD&psc=1&qid=1584126895'
    			]

    def parse(self, response):
        items = AmazoonItem()

        product_name = response.css()