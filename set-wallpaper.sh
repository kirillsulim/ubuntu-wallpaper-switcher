FILE=`pwd`/`\date '+%Y-%M-%dT%H%M%S'`
wget -O $FILE `./get_random_wallpaper_link.py`

sleep 5

gsettings set org.gnome.desktop.background picture-uri file://$FILE
