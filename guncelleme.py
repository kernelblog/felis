#!/usr/bin/env python3

import urllib.request
import os
import subprocess
import sys
import zipfile
from bs4 import BeautifulSoup
import ssl

url = "https://felis.kernelblog.org/tarih.txt"
url2 = "https://felis.kernelblog.org/felis/felis.zip"
context = ssl._create_unverified_context()

os.system("sudo pip3 install youtube-dl bs4 PrettyTable requests --upgrade")

try:
	url_oku = urllib.request.urlopen(url)
except urllib.error.URLError as e:
	print("\nLütfen İnternet Bağlantınızı Kontrol Ediniz!\n")
	sys.exit(0)
soup = BeautifulSoup(url_oku, 'html.parser')
if str(soup) == "24/09/2019":
	print("\nFelis Aracı Güncel.\n")
else:
	veri = urllib.request.urlopen(url2, context = context)
	f = open("felis.zip", 'wb')
	f.write(self.veri.read())
	f.close()
	feliszip = zipfile.ZipFile("felis.zip","r")
	feliszip.extractall(path=None, members=None)
	os.system("rm felis.zip")
	ls = subprocess.check_output(["ls", os.getcwd()+"/felis"])
	ls1=ls.decode("utf-8")
	ls2=ls1.find("yeni.py")
	if ls2 != -1:
		os.system("python3 "+os.getcwd()+"/yeni.py")
	else:
		pass
	os.system("sudo rm /usr/bin/felis")
	os.system("sudo rm /usr/share/felis/felis.py")
	os.system("sudo rm /usr/share/felis/mp.py")
	os.system("sudo rm /usr/share/felis/githubmodul.py")
	os.system("sudo rm /usr/share/felis/distrorepo.py")
	os.system("sudo mv "+os.getcwd()+"/felis/felis /usr/bin/")
	os.system("sudo mv "+os.getcwd()+"/felis/felis.py /usr/share/felis/")
	os.system("sudo mv "+os.getcwd()+"/felis/mp.py /usr/share/felis/")
	os.system("sudo mv "+os.getcwd()+"/felis/githubmodul.py /usr/share/felis/")
	os.system("sudo mv "+os.getcwd()+"/felis/distrorepo.py /usr/share/felis/")
	os.system("sudo chmod 755 /usr/bin/felis")
	os.system("sudo chmod 755 /usr/share/felis/felis.py")
	os.system("sudo chmod 755 /usr/share/felis/mp.py")
	os.system("sudo chmod 755 /usr/share/felis/githubmodul.py")
	os.system("sudo chmod 755 /usr/share/felis/distrorepo.py")
	print("\nFelis Aracınız Başarıyla Güncellenmiştir.\n")
	os.system("sudo mv "+os.getcwd()+"/felis/guncelleme.py /usr/share/felis/")
	os.system("rm -r felis")
