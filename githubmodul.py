#-*- coding: UTF-8 -*-
#!/usr/bin/env python3

import sys
import os
from bs4 import BeautifulSoup
import urllib.request
from prettytable import PrettyTable
import zipfile
import ssl

class github(object):

    def basla(self):
        self.isimler = []
        self.adresler = []
        self.gitadr = "https://github.com"
        self.zipadres = "/archive/master.zip"
        self.context = ssl._create_unverified_context()
        self.basitarama()

    def gitindir(self):
        os.system("git clone "+self.adresler[self.secim-1]+".git")
        sys.exit(0)

    def felisindir(self):
        self.zipadres = self.adresler[self.secim-1]+self.zipadres
        print("\nAraç İndiriliyor...")
        self.veri = urllib.request.urlopen(self.zipadres, context = self.context)
        f = open("arac.zip", 'wb')
        f.write(self.veri.read())
        f.close()
        araczip = zipfile.ZipFile("arac.zip","r")
        print("\nAraç Dosyaları Çıkartılıyor...")
        araczip.extractall(path=None, members=None)
        os.system("rm arac.zip")
        print("\nAraç başarıyla indirildi ve zipten çıkartıldı.")
        print("Vazgeçme :D.\n")
        sys.exit(0)

    def sirala(self):
        sequence = ["S.No", "Başlık"]
        t = PrettyTable(sequence)
        sz = len(self.isimler)
        print("\nSonuçlar bulundu = " + str(sz))
        sys.setrecursionlimit(100000)
        for i in range(sz):
            t.add_row([i + 1, self.isimler[i]])
        if len(self.isimler) != 0:
            print("\nSonuçlar : ")
            print(t)
            while True:
                self.secim = int(input("\nSeçiminizi girin (Sayısal): "))
                if self.secim > self.sayi or self.secim < 1:
                    print("\nSonuç sayısından fazla ya da eksik sayı girdiniz!")
                else:
                    break
            self.repobilgi()

    def repobilgi(self):
        self.baglan = urllib.request.urlopen(self.adresler[self.secim-1], context = self.context)
        self.sayfa = BeautifulSoup(self.baglan, 'html.parser')
        self.sayfa1 = self.sayfa.find_all("article",attrs={"class":"markdown-body entry-content p-5"})
        for i in self.sayfa1:
            print("\n")
            print(i.text)
        print("""\n1- Aracı git ile indir.\n2- Aracı felis ile indir.\n3- Listeye dön.\n""")
        while True:
            self.secenek = int(input("Seçiminizi girin (Sayısal): "))
            if self.secenek > 3 or self.secenek < 1:
                print("Hatalı girdi!\n")
            else:
                break
        if self.secenek == 1:
            self.gitindir()
        elif self.secenek == 2:
            self.felisindir()
        elif self.secenek == 3:
            self.sirala()

    def basitarama(self):
        self.isim = input("\nAramak istediğiniz aracın ismini giriniz: ")
        while True:
            self.sayi = int(input("Gösterilmesini istediğiniz sonuç sayısını giriniz: "))
            if (self.sayi % 10) == 0:
                break
            else:
                print("\nLütfen 10 ve katları olan bir sayı veriniz.\n")
        for e in range(0,int(self.sayi/10)):
            self.gitsrc = "https://github.com/search?p={}&q={}".format(str(e+1),self.isim)
            self.baglan = urllib.request.urlopen(self.gitsrc, context = self.context)
            self.sayfa = BeautifulSoup(self.baglan, 'html.parser')
            self.sayfa = self.sayfa.find_all("a",attrs={"class":"v-align-middle"})
            for i in self.sayfa:
                self.isimler.append(i.text)
                self.adresler.append(self.gitadr+i.get("href"))
        self.sirala()

if __name__ == '__main__':
    k = github()
    try:
        try:
            k.basla()
        except EOFError as e:
            print("\n\nİyi Akşamlarr :D")
    except KeyboardInterrupt as e:
        pass
