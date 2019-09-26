#-*- coding: UTF-8 -*-
#!/usr/bin/env python3
#KernelBlog Bağımsız Çalışma Programı

#Kütüphaneler
import sys
import os
import urllib.request
import zipfile
import tarfile
import requests
import ssl

def yardim():
	print("\nKullanım: felis [klon URL, -y, -g, -git, -depo, -s, -mp3, -mp4]")
	print("\n-y: Felis'in kullanımını ve parametreleri gösterir.\n-g: Felis'in güncellemelerini kontrol eder.\n-git: Github üzerinden araç arama moduna geçmenizi sağlar.\n-depo: Kali Linux ve Parrot Linux depoları üzerinden araç arama moduna geçmenizi sağlar.\n-s: Felis'i siler.\nklon: Araç indirme parametresidir.\n-mp3 şarkı_adı: Verilen şarkının mp3 dosyası indirir.\n-mp4 şarkı_adı: Verilen şarkının mp4 dosyası indirir.\n\nklon parametresi ile indirilecek dosya .zip, .deb veya .tar.gz uzantılı olmalıdır. İsterseniz klon parametresi ile GitHub'dan repo da indirebilirsiniz.\n")
	print("<======KernelBlog.org======>\nKernelBlog Developer Team\nKernelBlog Geliştirici Ekibi\n")

#Ana Bölüm
prefix=os.getenv("PREFIX","")
termux=len(prefix) > 1
if not termux:
	prefix="/usr"

sudo="" if termux else "sudo "

def internet_kontrol():
    url="http://www.google.com/"
    timeout=5
    try:
        test = requests.get(url, timeout=timeout)
    except requests.ConnectionError:
        print("\nLütfen İnternet Bağlantınızı Kontrol Ediniz!\n")
        sys.exit(0)

internet_kontrol()

if len(sys.argv) < 2 or sys.argv[1]=="-y":
		yardim()

elif sys.argv[1]=="-g":
	os.system("python3 "+prefix+"/share/felis/guncelleme.py")

elif sys.argv[1]=="-s":
	os.system(sudo+"rm "+prefix+"/bin/felis")
	print("\nFelis Başarıyla Kaldırıldı\n")
	os.system(sudo+"rm -r "+prefix+"/share/felis/")

elif sys.argv[1] == "-mp3":
    soru=input("\nGüncellemeler Kontrol Edilsin Mi? E/H: ")
    if soru == "e" or soru == "E":
        os.system("python3 "+prefix+"/share/felis/guncelleme.py")
    else:
        pass
    os.system("python3 "+prefix+"/share/felis/mp.py -mp3 "+sys.argv[2])

elif sys.argv[1] == "-mp4":
    soru=input("\nGüncellemeler Kontrol Edilsin Mi? E/H: ")
    if soru == "e" or soru == "E":
        os.system("python3 "+prefix+"/share/felis/guncelleme.py")
    else:
        pass
    os.system("python3 "+prefix+"/share/felis/mp.py -mp4 "+sys.argv[2])

elif sys.argv[1] == "-git":
    soru=input("\nGüncellemeler Kontrol Edilsin Mi? E/H: ")
    if soru == "e" or soru == "E":
        os.system("python3 "+prefix+"/share/felis/guncelleme.py")
    else:
        pass
    os.system("python3 "+prefix+"/share/felis/githubmodul.py")

elif sys.argv[1] == "-depo":
    soru=input("\nGüncellemeler Kontrol Edilsin Mi? E/H: ")
    if soru == "e" or soru == "E":
        os.system("python3 "+prefix+"/share/felis/guncelleme.py")
    else:
        pass
    os.system("python3 "+prefix+"/share/felis/distrorepo.py")

elif sys.argv[1]=="klon":
    context = ssl._create_unverified_context()
    try:
        try:
            url=sys.argv[2]
            urluzan=url[-5:]
            urluzantar=url[-8:]
            zip=urluzan.find(".zip")
            deb=urluzan.find(".deb")
            git=urluzan.find(".git")
            targz=urluzantar.find(".tar.gz")
        except IndexError as e:
            print("\nLütfen URL Giriniz!\n")
            sys.exit(0)

        soru=input("\nGüncellemeler Kontrol Edilsin Mi? E/H: ")
        if soru == "e" or soru == "E":
            os.system("python3 "+prefix+"/share/felis/guncelleme.py")
        else:
            pass

        if zip != -1:
            print("\nAraç İndiriliyor...")
            veri = urllib.request.urlopen(sys.argv[2], context = context)
            f = open("arac.zip", 'wb')
            f.write(veri.read())
            f.close()
            araczip = zipfile.ZipFile("arac.zip","r")
            print("\nAraç Dosyaları Çıkartılıyor...")
            araczip.extractall(path=None, members=None)
            os.system("rm arac.zip")
            print("\nAraç başarıyla indirildi ve zipten çıkartıldı.")
            print("Vazgeçme :D.\n")


        elif git != -1:
            os.system("git clone "+url)

        elif deb != -1:
            print("\nAraç İndiriliyor. İndirmenin Ardından Yükleme Otomatik Olarak Başlayacaktır...\n")
            veri = urllib.request.urlopen(sys.argv[2], context = context)
            f = open("arac.deb", 'wb')
            f.write(veri.read())
            f.close()
            os.system(sudo+"dpkg -i paket.deb")
            os.system("rm paket.deb")

        elif targz != -1:
            print("\nAraç İndiriliyor...")
            veri = urllib.request.urlopen(sys.argv[2], context = context)
            f = open("arac.tar.gz", 'wb')
            f.write(veri.read())
            f.close()
            targzac = tarfile.open("arac.tar.gz","r")
            print("\nAraç Dosyaları Çıkartılıyor...")
            targzac.extractall()
            targzac.close()
            os.system("rm arac.tar.gz")
            print("\nAraç başarıyla indirildi ve tar dosyasından çıkartıldı.")
            print("Vazgeçme :D.\n")

    except KeyboardInterrupt as e:
        print("\nFelis'ten Çıkılıyor.")
    else:
        pass

else:
        yardim()
