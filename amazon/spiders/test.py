import scrapy
class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
    'http://quotes.toscrape.com/page/1/',
    'http://www.google.com/',
    ]
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        # print(f'\n**************{page}**************\n')
        with open(filename, 'wb') as f:
            f.write(response.body)