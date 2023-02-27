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
for shows in konten:
    for show in shows:
        print(show.text)
