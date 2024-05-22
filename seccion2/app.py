from flask import Flask, request, redirect, url_for, render_template, Response, jsonify
import sqlite3


app = Flask(__name__)

app.secret_key = b'e3a777d9aeb11bef997bcdd30e7ecf58bf6d7186b24ecd382f253e3c51910162'
SQLITE_DB = 'usuarios.db'

def middleware(func):
    def wrapped(*args, **kwargs):
        username = request.authorization['username']
        password = request.authorization['password']
        if username == 'admin' and password == 'admin':
            return func(*args, **kwargs)
        return Response('Credenciales incorrectas', status=401)
    return wrapped


@app.route('/protegido', methods=['GET'])
@middleware
def protegido():
    return 'Ingreso correctamente'


@app.route('/obtener_usuario', methods=['GET'])
def obtener_usuario():
    user_id = request.args.get('user_id')
    if not user_id:
        return Response("Error, Falta el parametro 'user_id'", 400)
    try:
        conexion = sqlite3.connect(SQLITE_DB)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
            usuario_dict = {
                "id": usuario[0],
                "nombre": usuario[1],
                "email": usuario[2]
            }
            return jsonify(usuario_dict)
        else:
            return Response("Usuario no encontrado", status=404)
    except sqlite3.Error as e:
        return Response(f'Error al traer el registro de la db. {e}', status=500)
    
    
def iniciar_db():
    conexion = sqlite3.connect(SQLITE_DB)
    cursor = conexion.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('SELECT COUNT(*) FROM usuarios')
    count = cursor.fetchone()[0]

    if count == 0:
        usuarios = [
            ('Pedro Diaz', 'pedro@mail.com'),
            ('tomas', 'tomas@yahoo.com'),
            ('Cristian', 'cristian@hotmail.com'),
            ('Ricardo', 'ricardo@gmail.com'),
            ('Ricki', 'ricki@mail.com'),
            ('David', 'david@mail.com'),
        ]

        cursor.executemany('INSERT INTO usuarios (nombre, email) VALUES (?, ?)', usuarios)
        print(f'Se han insertado {len(usuarios)} registros de prueba en la tabla usuarios.')

    conexion.commit()
    conexion.close()

    
if __name__ == "__main__":
    iniciar_db()
    app.run(debug=True)