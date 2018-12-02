import urllib.request
import time

def solicitudHTTP(url): # En mi caso la url es 192.168.201.2
    inicio = time.time()
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        response.getheaders()
        final = time.time()
        b = response.getheader('Content-Length')

    tiempo = float(final-inicio)
    bytes = int(b)
    velocidad = int(bytes/tiempo)

    return [tiempo, bytes, velocidad]
