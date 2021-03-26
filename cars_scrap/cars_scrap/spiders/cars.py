import scrapy
import re 

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['www.datacvr.virk.dk']
    start_urls = ['https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id=69749917&soeg=coloplast&type=undefined&language=da/']

    def parse(self, response):
        regnskaber = response.xpath("//div[@class='aktive-regnskaber']/div[@class='regnskabBoksSide   regnskabBoksBund regnskabBoksTop  ']/div/div/div[@class='col-sm-12 regnskabs-periode']/child::node()").getall()
        for regnskab in regnskaber: 
            if re.match(r'\d{2}.\d{2}.\d{4}', regnskab): 
                periode = regnskab
                yield {
                    'Periode': periode,
                }


#//div[@class="aktive-regnskaber"]/div[@class="regnskabBoksSide   regnskabBoksBund regnskabBoksTop  "]/div/div/div[@class='col-sm-12 regnskabs-periode']