import scrapy 
from ..items import Scrapy2Item

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 1
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    id = 0
    def parse(self,response):
        
        items = Scrapy2Item()
        items2 = Scrapy2Item()
        all_div_quotes= response.css('div.quote')
        
        for quotes in all_div_quotes:

            quote = quotes.css('span.text::text').get()
            author = quotes.css('.author::text').get()
            tags = quotes.css('.tag::text').extract()
            
            QuoteSpider.id +=1
            items["id"]=QuoteSpider.id
            items["quote"]=quote
            items["author"] = author
            items["tags"] = tags
            yield items
        
        next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number)+'/'

        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)
