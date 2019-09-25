if [ $(id -g) -ne 0 ] || [ ! -n $PREFIX ]
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

mkdir /usr/share/felis
cp felis /usr/bin/
cp *.py /usr/share/felis/
chmod 755 /usr/bin/felis
chmod 755 /usr/share/felis/*

echo "Yükleme başarıyla tamamlandı. Terminale felis yazarak kullanabilirsiniz."
