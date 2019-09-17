#-*- coding: UTF-8 -*-
#KernelBlog Bağımsız Çalışma Programı

#Kütüphaneler
import sys
import os
import urllib.request
import zipfile
import tarfile
import requests

#Ana Bölüm
def internet_kontrol():
    url="http://www.google.com/"
    timeout=5
    try:
        test = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("\nLütfen İnternet Bağlantınızı Kontrol Ediniz!\n")
        sys.exit(0)
    return False

internet_kontrol()

if sys.argv[1]=="-y":
	print("\nKullanım: felis [klon URL, -y, -g, -s, -mp3, -mp4]")
	print("\n-y: Felis'in kullanımını ve parametreleri gösterir.\n-g: Felis'in güncellemelerini kontrol eder.\n-s: Felis'i siler.\nklon: Araç indirme parametresidir.\n-mp3: Verilen şarkının mp3 dosyası indirir.\n-mp4: Verilen şarkının mp4 dosyası indirir.\n\nBu uygulama ile indirilecek dosya .zip, .deb veya .tar.gz uzantılı olmalıdır. İsterseniz felis ile GitHub'dan repo da indirebilirsiniz.\n")
	print("<======KernelBlog.org======>\nKernelBlog Developer Team\nKernelBlog Geliştirici Ekibi\n")

elif sys.argv[1]=="-g":
	os.system("python3 /usr/share/felis/guncelleme.py")

elif sys.argv[1]=="-s":
	os.system("sudo rm /usr/bin/felis")
	print("\nFelis Başarıyla Kaldırıldı\n")
	os.system("sudo rm -r /usr/share/felis/")

elif sys.argv[1] == "-mp3":
    os.system("python3 /usr/share/felis/mp.py -mp3 "+sys.argv[2])

elif sys.argv[1] == "-mp4":
    os.system("python3 /usr/share/felis/mp.py -mp4 "+sys.argv[2])

elif sys.argv[1]=="klon":
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
            os.system("python3 /usr/share/felis/guncelleme.py")
        else:
            pass

        if zip != -1:
            print("\nAraç İndiriliyor...")
            urllib.request.urlretrieve(sys.argv[2], os.getcwd()+"/arac.zip")
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
            urllib.request.urlretrieve(sys.argv[2],os.getcwd()+"/paket.deb")
            os.system("sudo dpkg -i paket.deb")
            os.system("rm paket.deb")

        elif targz != -1:
            print("\nAraç İndiriliyor...")
            urllib.request.urlretrieve(sys.argv[2],os.getcwd()+"/arac.tar.gz")
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
