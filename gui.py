
# 1) Meget af teksten er dannet på baggrund af kald fra API'er, 
# det gør det umuligt at scrape uden at danne en DOM. 
# 2) Automatiseringen skal forgå enten vha. selenium, pyppeter eller lign.  

r = scrapy.Request(url="https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id=69749917&soeg=coloplast&type=undefined&language=da")

fetch(r)
aarsrapport = response.xpath("//*[@id='collapse_-Regnskaber-og-nogletal']/div[1]/div[2]")
aarsrapport.get()



//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[1]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[3]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[5]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[7]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[9]


//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[1]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[3]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[5]


//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[1]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[3]
//*[@id="collapse_-Regnskaber-og-nogletal"]/div[1]/div[2]/div[5]