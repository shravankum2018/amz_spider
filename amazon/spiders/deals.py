# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/deal-of-day/s?k=deal+of+the+day&page=5']

    def parse(self, response):
        for product in response.xpath("//div[contains(@class,'s-card-container')]"):
            yield{
                'title': product.xpath(".//span[contains(@class,'a-size-base-plus')]/text()").get(),
                # 'url': response.url(product.xpath(".//div[@class='sg-col-inner']//span//div//div//div//div//div[@class='a-section a-spacing-none a-spacing-top-small']//h2/a[@class='a-link-normal a-text-normal']/@href").get()),
                'discounted_price': product.xpath(".//span[contains(@class,'a-price-whole')]/text()").get(),
                # 'original_price': product.xpath(".//span[contains(@class,'a-text-price')]/span/text()").get() 
                'ID': product.xpath(".//span/a[contains(@href,'/dp/')]/@href").get(),

            }
