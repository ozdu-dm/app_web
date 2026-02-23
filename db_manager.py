import mysql.connector

# Configuración de conexión (XAMPP por defecto)
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'nom_mail' 
}

def conectar():
    """Establece la conexión con la BD"""
    return mysql.connector.connect(**config)

def buscar_mail_por_nombre(nombre):
    """Busca un mail dado un nombre. Retorna el mail o None."""
    conn = conectar()
    cursor = conn.cursor()
    
    # Buscamos el mail
    sql = "SELECT Mail FROM usuarios WHERE Nombre = %s"
    cursor.execute(sql, (nombre,))
    resultado = cursor.fetchone() # Devuelve una tupla (mail,) o None
    
    cursor.close()
    conn.close()
    
    if resultado:
        return resultado[0] # Devolvemos solo el string del mail
    return None

def agregar_usuario(nombre, mail):
    """Inserta un nuevo usuario. Retorna True si funciona, False si falla."""
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        sql = "INSERT INTO usuarios (Nombre, Mail) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, mail))
        conn.commit()
        
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error BD: {err}")
        return False