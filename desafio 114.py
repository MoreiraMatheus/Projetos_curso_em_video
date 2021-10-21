import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site não está disponivel.\033[m')
else:
    print('\033[32mO site está disponivel.\033[m')
