print("Teste de acessibilidade")
print("-" * 30)

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.youtube.com/feed/subscriptions")
except urllib.error.URLError:
    print("Erro ao acessar")
else:
    print("Tudo certo")
    #print(site.read())