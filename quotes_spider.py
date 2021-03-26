import scrapy


class CVRSpider(scrapy.Spider):
    name = 'cvr'
    start_urls = ['https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id=69749917&soeg=69749917&language=da',]

    def parse(self, response):
        for quote in response.css('id.collapse_-Regnskaber-og-nogletal'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
                }
