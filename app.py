from flask import Flask, render_template, request
import db_manager  # Módulo personalizado para manejar la base de datos

app = Flask(__name__, static_folder='estilos')

@app.route('/')
def home():
    # Redirigimos a la búsqueda por defecto
    return render_template('getmail.html')

# --- Ruta para BUSCAR (Get Mail) ---
@app.route('/getmail', methods=['GET', 'POST'])
def get_mail():
    resultado = None
    error = None
    
    if request.method == 'POST':
        nombre_buscado = request.form.get('nombre')
        
        if nombre_buscado:
            # Usamos la función del módulo db_manager
            mail_encontrado = db_manager.buscar_mail_por_nombre(nombre_buscado)
            
            if mail_encontrado:
                resultado = f"El mail de {nombre_buscado} es: {mail_encontrado}"
            else:
                error = f"No se encontró ningún usuario llamado {nombre_buscado}."
                
    return render_template('getmail.html', resultado=resultado, error=error)

# --- Ruta para AÑADIR (Add Mail) ---
@app.route('/addmail', methods=['GET', 'POST'])
def add_mail():
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mail = request.form.get('email')
        
        if nombre and mail:
            # Usamos la función del módulo db_manager
            exito = db_manager.agregar_usuario(nombre, mail)
            
            if exito:
                mensaje_exito = f"¡Usuario {nombre} registrado correctamente!"
            else:
                mensaje_error = "Hubo un error al guardar en la base de datos."
        else:
            mensaje_error = "Por favor, rellena todos los campos."
            
    return render_template('addmail.html', exito=mensaje_exito, error=mensaje_error)