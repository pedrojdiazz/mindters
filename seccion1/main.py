import re
import time
import os 

def lectorMails(archivo_texto):
    mail_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}'
    try: 
        with open(archivo_texto, 'r') as archivo:
            mails = archivo.read()
        matches = re.findall(mail_regex, mails)
        return len(matches)
    except FileNotFoundError as e:
        print(f'El archivo {archivo_texto} no fue encontrado')
        return 0


def tiempoEjecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f'Tiempo de ejecucion de la funcion: {fin - inicio} segundos')
        return resultado
    return wrapper


@tiempoEjecucion
def funcionEjemplo():
    time.sleep(3)
    print('Funcion ejecutada')

    
if __name__ == '__main__':
    print(f'Correos electronicos validos: {lectorMails('./seccion1/mails.txt')}')
    funcionEjemplo()