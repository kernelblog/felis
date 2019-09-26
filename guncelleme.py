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

prefix=os.getenv("PREFIX","")
termux=False
if len(prefix) > 1:
	termux=True
else:
	prefix="/usr"

sudo="" if termux else "sudo "

os.system(sudo+"pip3 install youtube-dl bs4 PrettyTable requests --upgrade")

try:
	url_oku = urllib.request.urlopen(url)
except urllib.error.URLError as e:
	print("\nLütfen İnternet Bağlantınızı Kontrol Ediniz!\n")
	sys.exit(0)
soup = BeautifulSoup(url_oku, 'html.parser')
if str(soup) == "25/09/2019":
	print("\nFelis Aracı Güncel.\n")
else:
	veri = urllib.request.urlopen(url2, context = context)
	f = open("felis.zip", 'wb')
	f.write(veri.read())
	f.close()
	feliszip = zipfile.ZipFile("felis.zip","r")
	feliszip.extractall(path=None, members=None)
	os.system("rm felis.zip")
	ls = os.popen("ls "+os.getcwd()+"/felis")
	ls = list(ls)
	for i in ls:
		i = i.replace("\n","")
		if i == "felis":
			os.system(sudo+"rm "+prefix+"/bin/felis")
			os.system(sudo+"mv "+os.getcwd()+"/felis/felis "+prefix+"/bin/")
			os.system(sudo+"chmod 755 "+prefix+"/bin/felis")
		elif i == "kur.sh":
			pass
		elif i == "ekstra.py":
			os.system("python3 "+os.getcwd()+"/felis/ekstra.py")
		else:
			os.system(sudo+"rm "+prefix+"/share/felis/"+i)
			os.system(sudo+"mv "+os.getcwd()+"/felis/"+i+" "+prefix+"/share/felis/")
			os.system(sudo+"chmod 755 "+prefix+"/share/felis/"+i)
	print("\nFelis Aracı Başarıyla Güncellendi.")
	os.system("rm -r felis")
