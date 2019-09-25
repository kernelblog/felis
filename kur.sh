if [ $(id -g) -ne 0 ]
then
	echo "Bu komutu sadece root erişimiyle çalıştırabilirsiniz"
	exit 1
fi

if [ -f /usr/bin/apt ] || [ -f $PREFIX/bin/apt ]
then
	apt update
	apt install python3 python3-pip git
fi

PIP_CMD="pip3"

if [ -f /usr/bin/pip3 ]
then
	PIP_CMD="/usr/bin/pip3"
elif [ -f $PREFIX/bin/pip ]
then
	PIP_CMD=$PREFIX"/bin/pip"
fi

exec PIP_CMD install beautifulsoup4 requests PrettyTable youtube_dl

#sudo apt-get install python3
#sudo apt-get install python3-pip
#sudo apt-get install git
#sudo pip3 install beautifulsoup4
#sudo pip3 install requests
#sudo pip3 install PrettyTable
#sudo pip3 install youtube_dl
sudo mkdir /usr/share/felis
sudo cp felis /usr/bin/
sudo cp felis.py /usr/share/felis/
sudo cp mp.py /usr/share/felis/
sudo cp githubmodul.py /usr/share/felis/
sudo cp distrorepo.py /usr/share/felis/
sudo cp guncelleme.py /usr/share/felis/
sudo chmod 755 /usr/bin/felis
sudo chmod 755 /usr/share/felis/felis.py
sudo chmod 755 /usr/share/felis/githubmodul.py
sudo chmod 755 /usr/share/felis/mp.py
sudo chmod 755 /usr/share/felis/guncelleme.py
sudo chmod 755 /usr/share/felis/distrorepo.py

echo "Yükleme başarıyla tamamlandı. Terminale felis yazarak kullanabilirsiniz."
