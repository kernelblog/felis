if [ $(echo $PREFIX | wc -c) -lt 2 ] && [ $(id -g) -ne 0 ]
then
	echo "Bu komutu sadece root erişimiyle çalıştırabilirsiniz"
	exit 1
fi

if [ -f /usr/bin/apt ]
then
	apt update
	apt install python3 python3-pip git
elif [ -f $PREFIX/bin/apt ]
then
	pkg install python git
fi

PIP_CMD="pip3"

if [ -f /usr/bin/pip3 ]
then
	PIP_CMD="/usr/bin/pip3"
elif [ -f $PREFIX/bin/pip ]
then
	PIP_CMD=$PREFIX"/bin/pip"
fi

$PIP_CMD install beautifulsoup4 requests PrettyTable youtube_dl

SETUP_ROOT="/usr"

if [ $(echo $PREFIX | wc -c) -gt 2 ]
then
	SETUP_ROOT=$PREFIX
fi

mkdir $SETUP_ROOT/share/felis 2>&1
cp felis $SETUP_ROOT/bin/
cp *.py $SETUP_ROOT/share/felis/
chmod 755 $SETUP_ROOT/bin/felis
chmod 755 $SETUP_ROOT/share/felis/*

echo "Yükleme başarıyla tamamlandı. Terminale felis yazarak kullanabilirsiniz."
