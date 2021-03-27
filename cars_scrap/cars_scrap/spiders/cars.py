import scrapy
import re 

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['www.datacvr.virk.dk']
    cvr='30359593'
    start_urls = [f'https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id={cvr}&soeg={cvr}&type=undefined&language=da/']
    

    def parse(self, response):
        self.virksomhed = response.xpath("//h1[@class='enhedsnavn']/text()").get()
        regnskaber = response.xpath("//div[@class='aktive-regnskaber']/div[@class='regnskabBoksSide   regnskabBoksBund regnskabBoksTop  ']")
        aarsrapporter = regnskaber.xpath(".//div[contains(text(),'Årsrapport')]/following-sibling::node()/a")

        for aarsrapport in aarsrapporter:
            titel = 'Aarsrapport'
            self.perioder = aarsrapport.xpath(".//parent::node()/parent::node()/parent::node()/parent::node()//div/div/div[@class='col-sm-12 regnskabs-periode']/child::node()").getall()[2] 
            href = aarsrapport.xpath(".//@href").get()
            self.datatype = aarsrapport.xpath(".//text()").get()

            yield response.follow(url=href, callback=self.save_pdf, dont_filter=True)
            # yield {
            #     'Virksomhed': virksomhed, 
            #     'Aarsrapporter': [
            #       {'Titel': titel,
            #       'Periode': perioder,
            #       'Link': href,
            #       'Type': datatype }]
            #     }
    
    
    def save_pdf(self, response):
        if 'PDF' in self.datatype:
            with open(f'{self.virksomhed}_aarsapport_{self.datatype}_{self.perioder}.pdf', 'wb') as f:
                f.write(response.body)  
        else:
            with open(f'{self.virksomhed}_aarsapport_{self.datatype}_{self.perioder}.xml', 'wb') as f:
                f.write(response.body)


#.//div[contains(text(),'Årsrapport')]

# Periode: 2020
# Filformat: PDF 
# Link: wwww._____________.dk






"""
1. hvis fil er pdf gem pdf - hvis fil er xbrl gem i andet format
2. start på ibm cloud 




{"Virksomhed" : "Coloplast", 
 "Årsrapport" : [
   {
     "PDF" : "www.href", 
     "XBRL" : "www.href",
   }
]  

Antagelser: 1. Hvis 2020 ikke findes, så er 2019 blevet scrapet. 
"""