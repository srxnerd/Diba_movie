import requests
from inscriptis import get_text
import sys
from time import sleep
from bs4 import BeautifulSoup
import re
import wget
import os
from urlextract import URLExtract
def print_slow_3(words):
    str(words)
    for char in str(words):
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
        char.replace("%","")
print_slow_3("Diba movie Download new film ;(  ")

more = input("\n 1.new movie  \n 2.Download the world's top 250 movies \n\n\nType(1 or 2): ")
if more == "1":
    extractor = URLExtract()


    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie = soup.find_all('h2' , class_="post-titles")

    for name_movie in link_movie:
        string = str(name_movie)
        urls = extractor.find_urls(string)
        dl_url = str(urls)
        ddr = dl_url.replace("[","")
        ddr = ddr.replace("]","")
        ddr = ddr.replace("'","")
        string_txt = get_text(string)

        sleep(1)
        print("\n\n",string_txt,"\n\nurl -->",ddr, "\n\n")
        dl = input("Do you want to download the movie Type(yes , no , exit): ")
        if dl == "yes":
            extractor_dl = URLExtract()
            url_dl = requests.get(ddr)
            url_new_dl = url_dl.text
            soup = BeautifulSoup(url_new_dl, "html.parser")
            link_movie_dl = soup.find_all('a' , class_="dublboxa")
            down = link_movie_dl
            for  a in down:
                if re.findall('http.*\.mkv', a['href']):
                    link_for_dl = a
                    string_for_dl = str(link_for_dl)
                    for_down = extractor.find_urls(string_for_dl)

                    downloader_db = str(for_down)
                    ddr_db = downloader_db.replace("[","")
                    ddr_db = ddr_db.replace("]","")
                    ddr_db = ddr_db.replace("'","")
                    print(ddr_db)
                    sleep(1)
                    os.system("mkdir  Diba_movie")
                    wget.download(ddr_db)
                    os.system("mv *.mkv /Diba_movie")
        if dl == "no":
            pass

        if dl == "exit":
            break
    extractor = URLExtract()
    link = requests.get("http://mydiba.link/top-250-imdb/")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    mydivs = soup.find_all('a', class_="bxof")
    my = str(mydivs)
    urls = extractor.find_urls(my)
    print(urls)
if more == "2":
    link = requests.get("http://mydiba.link/top-250-imdb/")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    mydivs = soup.find_all('', class_="budget")
    for div in mydivs:
        string = str(div)
        string_txt = get_text(string)
        sleep(1)
        print(string_txt,"\n")
