from HTTPbueno import *
from twogirlsoneCUPS import *
#Agregen sus importaciones

def main():
    print('Elige el sensor que quieres usar: ')
    print('1. Sensor SMTP')
    print('2. Sensor HTTP')
    print('3. Sensor FTP')
    print('4. Sensor CUPS')
    print('5. Sensor TELNET')

    opc = int(input('Selecciona tu opcion: '))
    if(opc==1):
        print('SMTP')
    elif(opc==2):
        url = input('Introduce la url del sitio web: ')
        [tiempo, bytes, velocidad] = solicitudHTTP(url)
        print('Tiempo de respuesta: ', tiempo)
        print('Bytes descargados: ', bytes)
        print('Ancho de banda: ' + str(velocidad) + ' bytes por segundo')
    elif(opc==3):
        print('FTP')
    elif(opc==4):
        impresora = input('Introduce la direccion de tu impresora: ')
        getinfoprinter(impresora)
    elif(opc==5):
        print('TELNET')
    else:
        print('No pusiste una opcion valida')

print('Buenas tardes, buenas noches, señoritas y señores')
repetir = 's'
while(repetir=='s' or repetir=='S'):
    main()
    repetir = input('Quieres repetir? s/n ')