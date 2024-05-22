import re
import time
import os
def lector_mails(archivo_texto):
    mail_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}'
    try: 
        with open(archivo_texto, 'r') as archivo:
            mails = archivo.read()
        matches = re.findall(mail_regex, mails)
        return len(matches)
    except FileNotFoundError as e:
        print(f'El archivo {archivo_texto} no fue encontrado')
        return 0


def tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f'Tiempo de ejecucion de la funcion: {round((fin - inicio), 2)} segundos')
        return resultado
    return wrapper


@tiempo_ejecucion
def funcionEjemplo():
    time.sleep(3)
    print('Funcion ejecutada')

    
if __name__ == '__main__':
    BASE_FILE = os.path.dirname(__file__)
    print(f'Correos electronicos validos: {lector_mails(os.path.join(BASE_FILE, 'mails.txt'))}')
    funcionEjemplo()