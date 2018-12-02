from httpCHIDO import *
from twogirlsoneCUPS import *
from smtp import *
from easysnmp import Session
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
        print('SMTP\n')
        from_host = "@".join([os.getenv("LOGNAME"), socket.gethostname()])
        usuario = input("Escribe el nombre de usuario destino: ")
        ip = input("Escribe la direccion ip del destino: ")
        dominio = input("Escribe el dominio: ")
        puerto = input("Escribe el puerto del dominio: ")
        sbj = "Comprobando el envío de correo localmente"
        txt = "Si puedes leer esto, tu servidor local SMTP está OK"
        send_mail_local(from_host, usuario, ip, dominio, puerto, sbj, txt)
        #print("Comprueba el correo en tu buzón local")
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
        session = Session(hostname='localhost', community="comunidadASR", version=2)
        print('TELNET')
        trafico_recibido=session.walk('1.3.6.1.2.1.2.2.1.10')
        trafico_enviado =session.walk('1.3.6.1.2.1.2.2.1.16')
        print("Trafico recibido: " + str(trafico_recibido))
        print("Trafico enviado: " + str(trafico_enviado))

    else:
        print('No pusiste una opcion valida')

print('Buenas tardes, buenas noches, señoritas y señores')
repetir = 's'
while(repetir=='s' or repetir=='S'):
    main()
    repetir = input('Quieres repetir? s/n ')
