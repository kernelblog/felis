#-*- coding: UTF-8 -*-
#!/usr/bin/env python3

import sys
import os
from bs4 import BeautifulSoup
import urllib.request
from prettytable import PrettyTable
import ssl

class distro(object):

    def basla(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        self.context = ssl._create_unverified_context()
        self.distrolar = []
        self.kontrol = 0
        self.isimler = []
        self.isimler1 = []
        self.isimler2 = []
        self.adresler = []
        self.adresler1 = []
        self.kaladr = "http://http.kali.org/kali/pool/"
        self.paradr = "http://deb.parrot.sh/parrot/pool/"
        self.bolumler = ["main/","contrib/","non-free/"]
        self.isim = input("\nAramak istediğiniz aracın ismini giriniz: ")
        self.isim = self.isim.lower()
        print("\n1- Aracı Parrot Linux depolarından ara.\n2- Aracı Kali Linux depolarından ara.\n3- Aracı her iki depodan da ara.")
        while True:
            try:
                self.distrosecim = int(input("\nDepo seçiniz (Sayısal): "))
                if self.distrosecim < 1 or self.distrosecim > 3:
                    print("Lütfen 1 ile 3 arasında bir seçim yapınız!")
                else:
                    break
            except ValueError as e:
                print("Sayısal diyoruz hocam!")
        if self.distrosecim == 1:
            self.distrolar.append(self.paradr)
        elif self.distrosecim == 2:
            self.distrolar.append(self.kaladr)
        else:
            self.distrolar.append(self.kaladr)
            self.distrolar.append(self.paradr)
        self.arama()

    def felisindir(self):
        self.debadres = self.adresler2[self.secim-1]
        print("\nAraç İndiriliyor...")
        self.istek = urllib.request.Request(url=self.debadres, headers = self.headers)
        self.veri = urllib.request.urlopen(self.istek, context = self.context)
        f = open(self.isimler4[self.secim-1], 'wb')
        f.write(self.veri.read())
        f.close()
        os.system("sudo dpkg -i "+self.isimler4[self.secim-1])
        os.system("sudo apt --fix-broken install")
        print("\nAraç başarıyla indirildi ve yüklendi.")
        self.soru = input("\nİndirilen dosya saklansın mı? E/H: ")
        if self.soru == "E" or self.soru == "e":
            print("\nDosyanız şu dizine kaydedildi ---> "+os.getcwd()+"/"+self.isimler4[self.secim-1])
            pass
        else:
            os.system("rm "+self.isimler4[self.secim-1])
        print("Vazgeçme :D.\n")
        sys.exit(0)

    def listele(self):
        self.isimler3 = []
        self.isimler4 = []
        self.adresler2 = []
        self.baglan = urllib.request.urlopen(self.adresler[self.secim-1], context = self.context)
        self.sayfa1 = BeautifulSoup(self.baglan, 'html.parser')
        self.sayfa1 = self.sayfa1.find_all("a")
        for i in self.sayfa1:
            self.isimler3.append(i.text)
        for i in self.isimler3:
            if i[-4:] == ".deb":
                self.isimler4.append(i)
                self.adresler2.append(self.adresler[self.secim-1]+i)
            else:
                pass
        self.sirala(self.isimler4, 1)
        print("""\n1- Felis ile indir.\n2- Listeye dön.\n""")
        while True:
            try:
                self.secenek = int(input("İşlem seçiniz (Sayısal): "))
                if self.secenek > 2 or self.secenek < 1:
                    print("Hatalı girdi!\n")
                else:
                    break
            except ValueError as e:
                print("Sayısal diyoruz hocam!")
        if self.secenek == 1:
            while True:
                try:
                    self.secim = int(input("\nİndirmek istediğiniz dosyayı seçiniz (Sayısal): "))
                    if self.secim < 1 or self.secim > len(self.isimler4):
                        print("Sonuç sayısından fazla ya da eksik bir sayı girdiniz!")
                    else:
                        break
                except ValueError as e:
                    print("Sayısal diyoruz hocam!")
            self.felisindir()
        else:
            self.sirala(self.isimler1, 0)

    def sirala(self, isimler, durum):
        self.basliklar = ["S.No", "Başlık"]
        t = PrettyTable(self.basliklar)
        sz = len(isimler)
        sys.setrecursionlimit(100000)
        if sz != 0:
            print("\nSonuçlar bulundu =",sz)
            for i in range(sz):
                t.add_row([i + 1, isimler[i]])
            print("\nSonuçlar : ")
            print(t)
            if durum == 0:
                while True:
                    try:
                        self.secim = int(input("\nSeçiminizi girin (Sayısal): "))
                        if self.secim > sz or self.secim < 1:
                            print("Sonuç sayısından fazla ya da eksik bir sayı girdiniz!")
                        else:
                            break
                    except ValueError as e:
                        print("Sayısal diyoruz hocam!")
                self.listele()
            else:
                pass
        else:
            self.kontrol += 1
            if self.kontrol > 2:
                print("\nAraç Bulunamadı.\n")
            else:
                self.arama()

    def arama(self):
        for distro in self.distrolar:
            self.baglan = urllib.request.urlopen(distro+self.bolumler[self.kontrol]+self.isim[0], context = self.context)
            self.sayfa = BeautifulSoup(self.baglan, 'html.parser')
            self.sayfa = self.sayfa.find_all("a")
            if distro == self.kaladr:
                for i in self.sayfa:
                    self.isimler.append(i.text)
                for i in self.isimler:
                    self.ara = i.find(self.isim)
                    if self.ara != -1:
                        self.isimler1.append("Kali --> "+i)
                        self.adresler.append(distro+self.bolumler[self.kontrol]+self.isim[0]+"/"+i)
                    else:
                        pass
                self.isimler.clear()
            else:
                for i in self.sayfa:
                    self.isimler.append(i.text)
                for i in self.isimler:
                    self.ara = i.find(self.isim)
                    if self.ara != -1:
                        self.isimler2.append("Parrot --> "+i)
                        self.adresler1.append(distro+self.bolumler[self.kontrol]+self.isim[0]+"/"+i)
                    else:
                        pass
        self.isimler1 += self.isimler2
        self.adresler += self.adresler1
        self.sirala(self.isimler1, 0)

if __name__ == '__main__':
    k = distro()
    try:
        try:
            k.basla()
        except EOFError as e:
            print("\n\nİyi Akşamlarr :D")
    except KeyboardInterrupt as e:
        pass
