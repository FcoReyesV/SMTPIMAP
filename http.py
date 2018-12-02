import requests
import time
inicio = time.time()
r = requests.get('http://192.168.201.2')
headers = r.headers
content = r.content
fin = time.time()

print(headers)

tiempo = float(fin-inicio)
bytes = int(headers['Content-Length'])
velocidad = int(bytes/tiempo)

print('Tiempo de respuesta: ', tiempo)
print('Número de bytes recibidos: ', bytes)
print('Velocidad de descarga: ' +  str(velocidad) + ' bytes por segundo')

