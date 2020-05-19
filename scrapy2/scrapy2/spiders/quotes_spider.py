import scrapy 
from ..items import Scrapy2Item

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):

        items = Scrapy2Item()

        all_div_quotes= response.css('div.quote')
        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
        