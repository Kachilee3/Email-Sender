
import os, platform, requests, webbrowser
from os import path,system
from platform import uname 

os.system('pip install requests')
os.system('termux-setup-storage')
os.system('xdg-open https://wa.me/2349035850097')
os.system( 'pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install pycryptodomex')
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support This Tool\033[1;37m")
    os.system('pip install stdiomask')
if __name__=='__main__':
 try:
  __import__("EmailSender").license()
 except Exception as e:
  exit(str(e))
elif bit == '32bit':
    print("\033[1;32;40mYour Device 32bit You Need A 64bit Device To Run This Tool")