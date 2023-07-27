'''Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mDeu erro\033[m')
else:
    print("\033[32mO site está funcionando\033[m")
    print(site.read())