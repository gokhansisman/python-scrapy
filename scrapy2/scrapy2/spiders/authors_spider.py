import scrapy 
from ..author import Scrapy2Item

class QuoteSpider(scrapy.Spider):
    name = 'authors'
    page_number = 1
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    _quote = 0
    def parse(self,response):
        
        author = Scrapy2Item()
        all_div_quotes= response.css('div.quote')
        
        
        for quotes in all_div_quotes:
            link = quotes.xpath('//span/a/@href').get()
            author_url = 'http://quotes.toscrape.com' + link+'/'
            yield scrapy.Request((response.urljoin(author_url)),callback=self.parse_dir_contents)

            yield response.follow('http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number)+'/',callback=self.parse)
        
        next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number)+'/'

        if QuoteSpider.page_number < 2:
            QuoteSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)
    def parse_dir_contents(self, response):
        author = response.xpath('//div[@class = "author-details"]/h3/text()').get() 
        print(author)
        QuoteSpider._quote += 1
        author["_quote"] = QuoteSpider._quote
        author["born"]="born"
        author["author"] = author
        author["description"] = "deneme"
        yield author
