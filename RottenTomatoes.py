from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import requests
import time
import json

PATH = "D:\Politeknik Negeri Bandung\B-TIF4'22\Semester 2\Proyek 1\Praktikum 4\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://editorial.rottentomatoes.com/guide/best-netflix-shows-and-movies-to-binge-watch-now/")

j = 1
konten = []
while j <= 100:
    konten.append(driver.find_elements(By.ID, "row-index-"+str(j)))
    j += 1

i = 1
showlist = []
for shows in konten:
    for show in shows:
        print(show.text)
        for img in show.find_elements(By.TAG_NAME, "img"):
            print(img.get_attribute("src")+"\n")
            #urllib.request.urlretrieve(img.get_attribute("src"), "Netflix Top"+ str(i)+".png")
            showlist.append(
                 {"Ranking": show.text.split("\n")[2],
                  "Judul": show.text.split("\n")[0],
                  "Tomato Meter": show.text.split("\n")[1],
                  "Image": img.get_attribute("src")
                 }
            )
            i = i+1

hasil_scrapping = open("HasilScrappingTomato.json", "w")
json.dump(showlist, hasil_scrapping, indent=6)
hasil_scrapping.close
driver.quit()
