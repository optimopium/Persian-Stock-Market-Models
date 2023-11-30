import scrapy
from crawlers.items import DatabourseItem


class DatabourseSpider(scrapy.Spider):
    name = 'databourse'
    allowed_domains = ['databourse.ir']
    start_urls = ['http://databourse.ir/marketwatch']

    def parse(self, response):
        # Select all rows in the table with id 'marketWatch'
        rows = response.xpath('//table[@id="marketWatch"]/tbody/tr')
        for row in rows:
            # For each row, go to the symbol and yield a request to the symbol's page
            symbol_path = row.xpath('td[@class="symbol"]/a/@href').get()
            if symbol_path:
                base_url = "https://databourse.ir"
                yield response.follow(base_url + symbol_path, self.parse_symbol_page)

    @staticmethod
    def parse_symbol_page(response):
        # Create an instance of the item
        item = DatabourseItem()
        # Extract the details using XPath
        item['symbol'] = response.xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/text()').get()
        item['company_name'] = response.xpath('//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/text()').get()
        item['bazaar'] = response.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[2]/span[2]/text()').get()
        item['bazaar_group'] = response.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[3]/span[2]/a/text()').get()

        yield item
