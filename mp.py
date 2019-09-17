#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import sys
import time
import os
import youtube_dl

def input_query():
    try:
        search_query = sys.argv[2:]
        if len(sys.argv) <= 1:
            raise IndexError
        return ' '.join(search_query)
    except IndexError:
        print("Hatalı Kullanım.")
        print("Örnek kullanım; felis -mp3 şarkı_adı veya felis -mp4 şarkı_adı")
        sys.exit()


def scrape():
    search_query = input_query()
    youtube_url = "https://www.youtube.com/results?search_query=" + search_query
    useragent = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    header = useragent
    try:
        response = requests.get(youtube_url, headers=header)
        if response.status_code == 200:
            print("\nŞarkı listesi alındı. Beklerken sonraki indireceğin parçayı düşünebilirsin.: ")
            time.sleep(2)
    except requests.exceptions.ConnectionError:
        print("\nBağlantı hatası. İnternet bağlantınızı kontrol edin veya bir süre sonra tekrar deneyiniz.")
        sys.exit()

    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    title = []
    ref = []
    all_title_tags = soup.find_all("h3", attrs={"class": "yt-lockup-title"})
    for h3 in all_title_tags:
        title.append(h3.find('a').contents[0])
        ref.append(h3.find('a')['href'])
    sequence = ["S.No", "Başlık"]
    t = PrettyTable(sequence)
    sz = len(title)
    print("Sonuçlar bulundu = " + str(sz))
    sys.setrecursionlimit(100000)
    for i in range(sz):
        t.add_row([i + 1, title[i]])
    if len(title) != 0:
        print("\nSonuçlar : ")
        print(t)
        choice = input("\nSeçiminizi girin (sayısal) : ")
        if 1 <= int(choice) <= len(title):
            filename = title[int(choice) - 1]
            video_url = "https://www.youtube.com" + str(ref[int(choice) - 1])
            return filename, video_url
        else:
            print("Geçersiz Girdi.")
            sys.exit()
    else:
        print("Üzgünüm,sonuç bulunamadı.")



def mp3indir():
    filename, video_url = scrape()
    print("Mp3 indiriliyor...")
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',}],
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Mp3 başarıyla indirildi.")
    sys.exit(0)


def mp4indir():
    filename, video_url = scrape()
    print("Mp4 indiriliyor...")
    ydl_opts = {
            'format': 'best',
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Mp4 başarıyla indirildi.")
    sys.exit(0)


if __name__ == "__main__":
    if sys.argv[1] == "-mp3":
        mp3indir()
    elif sys.argv[1] == "-mp4":
        mp4indir()
    else:
        print("Örnek kullanım; felis -mp3 şarkı_adı veya felis -mp4 şarkı_adı")
        sys.exit(0)
