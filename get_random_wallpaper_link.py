#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os
import random

FILE = 'file.jpg'

def get_wallhaven_random():
     resp = requests.get("https://alpha.wallhaven.cc/search?categories=100&resolutions=1920x1080%2C1920x1200%2C2560x1440%2C2560x1600%2C3840x1080%2C5760x1080%2C3840x2160%2C5120x2880&sorting=random")
     #resp = requests.get("https://alpha.wallhaven.cc/random")
     soup = BeautifulSoup(resp.text, 'html.parser')
     link = random.choice(soup.find_all('a', 'preview'))['href']
     resp = requests.get(link)
     soup = BeautifulSoup(resp.text, 'html.parser')
     link = 'http:' + soup.find(id='wallpaper')['src']
     return link

def set_windows_wallpaper(file):
     print('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d ' + file + ' /f')
     os.system('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d ' + file + ' /f')
     os.system('RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters')


link = get_wallhaven_random()
print (link)
#r = requests.get(link, stream=True)
#if r.status_code == 200:
     #with open(FILE, 'wb') as f:
         #for chunk in r:
             #f.write(chunk)

#set_windows_wallpaper(os.path.join(os.getcwd(), FILE))
