# -*- coding: utf-8 -*-

#Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os

#Define file path
webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
image_path = os.path.normpath(os.getcwd()+"\\photos")

#Add new search key into array ["Neymar visage","Mbappe visage","Marquinhos visage","verratti visage"]
search_keys= ["neymar official face photo"]

#Parameters
number_of_images = 300
headless = False
min_resolution=(0,0)
max_resolution=(1000,1000)

#Main program
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scrapper.find_image_urls()
    image_scrapper.save_images(image_urls)