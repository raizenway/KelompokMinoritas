from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import requests
import time

PATH = "D:\Politeknik Negeri Bandung\B-TIF4'22\Semester 2\Proyek 1\Praktikum 4\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://myanimelist.net/topanime.php")

konten = driver.find_elements(By.CLASS_NAME, "ranking-list")
imgMAL = driver.find_elements(By.XPATH,"//img[contains(@class,'lazyloaded')]")

i = 1
while i <=100:
    for anime in konten:
        print(anime.text)
        for img in anime.find_elements(By.TAG_NAME, "img"):
            print(img.get_attribute("data-src"))
            urllib.request.urlretrieve(img.get_attribute("data-src"), str(i)+".png")
            i = i+1
    try:
        driver.find_element(By.CLASS_NAME, "pagination").find_element(By.PARTIAL_LINK_TEXT,"Next").click()
    except NoSuchElementException as e:
        break;

"""
src = []
for anime in konten:
    print(anime.text)
    for img in anime.find_elements(By.XPATH,"//img[contains(@class,'lazyloaded')]"):
        src.append(img.get_attribute('data-src'))
        urllib.request.urlretrieve(img.get_attribute("data-src"), str(i)+".png")
        i = i+1"""
        
#for img in imgMAL:
    #src.append(img.get_attribute('data-src'))

#print(src[0])
driver.quit()
