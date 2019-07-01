#!/usr/bin/env python3
# -*- coding: utf8 -*-
#import lib
import webbrowser
from colored import fore, back, style
import requests
from inscriptis import get_text
import sys
from time import sleep
from bs4 import BeautifulSoup
import re
import wget
import os
from urlextract import URLExtract
from lxml import etree
from lxml import html

def print_slow_3(words):
    str(words)
    words = fore.GREEN + back.BLACK + words +style.RESET
    for char in str(words):
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        char.replace("%","")

def Points():
    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie_pints = soup.find_all('div' , class_="post-infos-index")
    for point in link_movie_pints:
        point = str(point)
        urls_point = get_text(point)
        sleep(1)
        print("About the movie\n\n","IMdb",urls_point,"\n\n")
os.system("clear")
def film():
    extractor = URLExtract()
    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie = soup.find_all('h2' , class_="post-titles")
    link_movie_pints = soup.find_all('div' , class_="post-infos-index")
    for point in link_movie_pints:
        point = str(point)
        urls_point = get_text(point)


    data = urls_point
    print(data)
    for name_movie in link_movie:
        string = str(name_movie)
        urls = extractor.find_urls(string)
        dl_url = str(urls)
        ddr = dl_url.replace("[","")
        ddr = ddr.replace("]","")
        ddr = ddr.replace("'","")
        string_txt = get_text(string)
        sleep(1)
        print("\n",string_txt,"\n\nurl -->",ddr, "\n\n")
def movie():

    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie_pints = soup.find_all('article' , class_="movie")
    soup.find('div', class_="ages").decompose()
    for point in link_movie_pints:
        show_link = point.find_all('h2' , class_="post-titles")
        extractor = URLExtract()
        point = str(point)
        urls_point = get_text(point)
        urls_imdb = show_link
        str_url = str(urls_imdb)
        ext = extractor.find_urls(str_url)
        dl_url = str(ext)
        ddr = dl_url.replace("[","")
        ddr = ddr.replace("]","")
        ddr = ddr.replace("'","")
        d_tir = ddr
        sleep(1)

        print(fore.RED + back.BLACK +"[---]                       [#]   PGS   [#]                    [---]"+style.RESET)
        print(fore.RED + back.BLACK +"[---]                 ~ github.com / stinerd  ~                [---]"+style.RESET)
        print(fore.RED + back.BLACK +"[---]                ~ Welcome to  Diba Movie ~                [---]"+style.RESET)
        print(fore.RED + back.BLACK +"[---]______________________Linux for life______________________[---]\n\n"+style.RESET)
        print(fore.GREEN + back.BLACK +"Link :-->"+style.RESET,fore.RED+ back.BLACK +ddr+style.RESET,"\n",fore.WHITE+ back.BLACK +urls_point+style.RESET,"\n")

        print(fore.CYAN + back.BLACK +"______________________________________________________________________\n")
        dl = input("Select iteme  \n1) [d] Download \n2) [N] Next_Movie\n3) [e] exit\n4) [s] Serial Playing\n5) [t] Triler Movie\n________________________________\n\n[#] -> ")
        if dl == "d":
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
                    print("link download: ->", ddr_db)
                    wget.download(ddr_db)
                    os.system("mv *.mkv /Diba_movie")
        if dl == "n" or dl == "N":
            os.system("clear")
            pass

        if dl == "exit" or dl == "e":
            sys.exit()

        if dl == "t":
            #triler Movie
            extractor = URLExtract()
            req = requests.get(ddr)
            tree = html.fromstring(req.text)
            req_t = req.text
            soup_tir = BeautifulSoup(req_t, "lxml")
            data_mv  = soup_tir.find('div', class_="-video")
            dn  = data_mv
            dn = str(dn)
            tri_link =extractor.find_urls(dn)
            tri_link = str(tri_link)
            dop = tri_link.replace("[","")
            dop_1 = dop.replace("]","")
            dop_2 = dop_1.replace("'","")
            dop_3 = re.findall('http://tr.*\.mp4', dop_2)
            # down_tt = tri_link.endswith('.mp4')
            dop_4 = str(dop_3)
            dop_4 = dop_4.replace("[","")
            dop_4 = dop_4.replace("]","")
            dop_4 = dop_4.replace("'","")
            os.system("mpv "+dop_4)


            sleep(5)

        if dl == "s":
            os.system("clear")
            extractor = URLExtract()
            #Serial
            Serial = requests.get("http://mydiba.link/series/?status=1&order=1")
            Serial_str = Serial.text
            soup_serial = BeautifulSoup(Serial_str, "html.parser")
            data_serial =soup_serial.find_all('a' , class_="col-xs-6 no-padding arch_series_fix")

            for ser in data_serial:
                rateser = ser.find('p', class_="rateser")
                name = ser.find('p', class_="titser")
                kifi = ser.find('p', class_="ser_q")
                dete = ser.find('p', class_="left ticks")
                updtsr = ser.find('p', class_="updtsr")

                str_rateser = str(rateser)
                str_rateser = get_text(str_rateser)
                str_name = str(name)
                str_name = get_text(str_name)
                str_dete = str(dete)
                str_dete = get_text(str_dete)
                str_kifi = str(kifi)
                str_kifi = get_text(str_kifi)
                str_updtsr = str(updtsr)
                str_updtsr = get_text(str_updtsr)
                ser.find('img', class_="serimg").decompose()
                ser_str = str(ser)
                done_serial = get_text(ser_str)
                url_serial = extractor.find_urls(ser_str)
                url_serial = str(url_serial)
                url_serial = url_serial.replace("]" , "")
                url_serial = url_serial.replace("[" , "")
                url_serial = url_serial.replace("'" , "")



                print(fore.GREEN + back.BLACK +"Link :-->"+style.RESET,fore.RED+ back.BLACK +url_serial+style.RESET,"\n",fore.BLUE + back.BLACK +str_name+style.RESET,"\n\npoints: ⤵️",str_rateser,"\n\nQuality: ⤵️",str_kifi,"\n\nDate: ⤵️",str_dete,"\n\nSection: ⤵️",str_updtsr)
                print(fore.CYAN + back.BLACK +"______________________________________________________________________\n")
                dl_serial = input("\n\nSelect iteme\n1) [n] Next Movie\n2) [e] Exit\n3) [o] Open link\n4) [t] Triler Serial    \n\n[#] ->  ") 
                os.system('clear')
                if dl_serial == "e":
                    sys.exit()
                if dl_serial == "o":
                    webbrowser.open(url_serial)
                if dl_serial == "d":
                    extractor_dl = URLExtract()
                    url_dl = requests.get(url_serial)
                    url_new_dl = url_dl.text
                    soup = BeautifulSoup(url_new_dl, "html.parser")
                    link_movie_dl = soup.find_all('div', class_="Block_links")
                    ser_str = str(link_movie_dl)
                    ser_dl = extractor.find_urls(ser_str)
                    str_dl = str(ser_dl)
                    dop = str_dl.replace("[","")
                    dop_1 = dop.replace("]","")
                    dop_2 = dop_1.replace("'","")
                    ser_dd = re.findall('http.*\.1080p.WEB-DL.6CH.DibaMovie.mkv', dop_2)
                    print(ser_dd)
                    sleep(2)
                if dl_serial == "t":

                    extractor = URLExtract()
                    req = requests.get(url_serial)
                    tree = html.fromstring(req.text)
                    req_t = req.text
                    soup_tir = BeautifulSoup(req_t, "lxml")
                    data_mv  = soup_tir.find('div', class_="-video")
                    dn  = data_mv
                    dn = str(dn)
                    tri_link =extractor.find_urls(dn)
                    tri_link = str(tri_link)
                    dop = tri_link.replace("[","")
                    dop_1 = dop.replace("]","")
                    dop_2 = dop_1.replace("'","")
                    dop_3 = re.findall('http://tr.*\.mp4', dop_2)
                    # down_tt = tri_link.endswith('.mp4')
                    dop_4 = str(dop_3)
                    dop_4 = dop_4.replace("[","")
                    dop_4 = dop_4.replace("]","")
                    dop_4 = dop_4.replace("'","")
                    os.system("mpv "+dop_4)






    extractor = URLExtract()
    link = requests.get("http://mydiba.link/top-250-imdb/")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    mydivs = soup.find_all('a', class_="bxof")
    my = str(mydivs)
    urls = extractor.find_urls(my)


movie()
