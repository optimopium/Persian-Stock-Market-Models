import scrapy


class DatabourseItem(scrapy.Item):
    symbol = scrapy.Field()
    company_name = scrapy.Field()
    bazaar = scrapy.Field()
    bazaar_group = scrapy.Field()