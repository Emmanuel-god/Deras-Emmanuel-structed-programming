import mysql.connector

# Conexión a la base de datos
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca"
    )
except mysql.connector.Error as e:
    print(f"Error al conectar a la base de datos: {e}")
    exit()

cursor = conexion.cursor()

def pedir_entero(mensaje):
    """Solicita un número entero utilizando recursividad."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("Debes ingresar un número.")
        return pedir_entero(mensaje)

# ===============================
# CRUD
# ===============================

def registrar_libro():
    print("\n--- REGISTRAR LIBRO ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = pedir_entero("Año: ")
    disponibles = pedir_entero("Cantidad disponible: ")

    sql = """
    INSERT INTO libros (titulo, autor, anio, disponibles)
    VALUES (%s, %s, %s, %s)
    """
    valores = (titulo, autor, anio, disponibles)

    cursor.execute(sql, valores)
    conexion.commit()
    print("Libro registrado correctamente.")

def consultar_libros():
    print("\n--- LISTA DE LIBROS ---")
    sql = "SELECT * FROM libros"
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        print("No existen registros.")
        return

    for libro in registros:
        print(f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]} | Disponibles: {libro[4]}")

def buscar_libro():
    print("\n--- BUSCAR LIBRO ---")
    id_libro = pedir_entero("ID del libro: ")
    sql = "SELECT * FROM libros WHERE id=%s"
    cursor.execute(sql, (id_libro,))
    libro = cursor.fetchone()

    if libro is None:
        print("Libro no encontrado.")
    else:
        print(f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]} | Disponibles: {libro[4]}")

def actualizar_libro():
    print("\n--- ACTUALIZAR LIBRO ---")
    id_libro = pedir_entero("ID del libro a actualizar: ")
    nuevos_disponibles = pedir_entero("Nueva cantidad disponible: ")

    sql = "UPDATE libros SET disponibles=%s WHERE id=%s"
    cursor.execute(sql, (nuevos_disponibles, id_libro))
    conexion.commit()

    if cursor.rowcount == 0:
        print("No se encontró el libro.")
    else:
        print("Libro actualizado correctamente.")

def eliminar_libro():
    print("\n--- ELIMINAR LIBRO ---")
    id_libro = pedir_entero("ID del libro a eliminar: ")

    sql = "DELETE FROM libros WHERE id=%s"
    cursor.execute(sql, (id_libro,))
    conexion.commit()

    if cursor.rowcount == 0:
        print("No se encontró el libro.")
    else:
        print("Libro eliminado correctamente.")

# ===============================
# MENÚ
# ===============================

def mostrar_menu():
    print("\n SISTEMA DE BIBLIOTECA")
    print("**************************")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Actualizar libro")
    print("5. Eliminar libro")
    print("6. Salir")

# ===============================
# PROGRAMA PRINCIPAL
# ===============================

def main():
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = pedir_entero("Seleccione una opción: ")

        if opcion == 1:
            registrar_libro()
        elif opcion == 2:
            consultar_libros()
        elif opcion == 3:
            buscar_libro()
        elif opcion == 4:
            actualizar_libro()
        elif opcion == 5:
            eliminar_libro()
        elif opcion == 6:
            print("\nPrograma finalizado.")
        else:
            print("Opción no válida.")

    cursor.close()
    conexion.close()

main()
