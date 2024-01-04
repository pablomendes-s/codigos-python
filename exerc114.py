import urllib
import urllib.request


try:
    site = urllib.request.urlopen('https://www.clickjogos.com.br/')
except:
    print("Deu ERRO!")
else:
    print("Acess ou")