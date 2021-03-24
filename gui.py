from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id=69749917&soeg=69749917&language=da")

elem1 = driver.find_element_by_class_name("cpAcceptBtn")
if elem1:
    elem1.click()

elem = driver.find_element_by_link_text("Regnskaber")

elem.click()


#collapse_-Regnskaber-og-nogletal > div.accordion-inner > div.aktive-regnskaber > div:nth-child(1) > div > div:nth-child(8) > div.col-sm-5.regnskabs-download > a
document.querySelector("#collapse_-Regnskaber-og-nogletal > div.accordion-inner > div.aktive-regnskaber > div:nth-child(3) > div > div:nth-child(7) > div.col-sm-5.regnskabs-download > a")
document.querySelector("#collapse_-Regnskaber-og-nogletal > div.accordion-inner > div.aktive-regnskaber > div:nth-child(1) > div > div:nth-child(6) > div.col-sm-5.regnskabs-download > a")