"""" 
This scripts scrapes all the different links from cvrlink.csv, and 
outputs an json file in the following format. If the link does 
not exist, it will continue to the next one. 

Concurrent scrapers: 3, 
Delay between: 1 sek.,  
Total duration: approximately 4 hours. 

{"Virksomhed" : "Coloplast", 
 "Årsrapport" : [
   {
     "PDF" : "www.href", 
     "XBRL" : "www.href",
   }
]  
"""


from scrapy.http.request import Request
import scrapy
import re 


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['www.datacvr.virk.dk']
    #cvr='30359593'
    #start_urls = [f'https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id={cvr}&soeg={cvr}&type=undefined&language=da/']
    
    def start_requests(self):
        with open('cvrlink.csv', 'rb') as cvrs:
            for line in cvrs:
                line = line.rstrip()
                line = line.decode()
                yield Request(line, self.parse, dont_filter = True)

    def parse(self, response):
        cvr = response.xpath("//div/h2/child::node()[contains(text(),'CVR-nummer')]/parent::node()/parent::node()/following-sibling::node()/text()").get().strip()
        virksomhed = response.xpath("//h1[@class='enhedsnavn']/text()").get()
        regnskaber = response.xpath("//div[@class='aktive-regnskaber']/div[@class='regnskabBoksSide   regnskabBoksBund regnskabBoksTop  ']")
        aarsrapporter = regnskaber.xpath(".//div[contains(text(),'Årsrapport')]/following-sibling::node()/a")


        for aarsrapport in aarsrapporter:
            perioder = aarsrapport.xpath(".//parent::node()/parent::node()/parent::node()/parent::node()//div/div/div[@class='col-sm-12 regnskabs-periode']/child::node()").getall()[2] 
            href = aarsrapport.xpath(".//@href").get()
            datatype = aarsrapport.xpath(".//text()").get()

            yield {
                'CVR': cvr,
                'Virksomhed': virksomhed, 
                'Aarsrapporter': [
                  {'Periode': perioder,
                   'Type': datatype,
                   'Link': href}
                   ]
                }

