db = {}


def mostrar_menu():
    print("\n--- Sistema CRUD ---")
    print("1. Crear | 2. Leer | 3. Actualizar | 4. Eliminar | 5. Salir")


def crear(id, nombre):
    db[id] = nombre
    print(f"Creado: {id} - {nombre}")


def leer():
    print("Registros actuales:", db)


def actualizar(id, nuevo_nombre):
    if id in db:
        db[id] = nuevo_nombre
        print(f"Actualizado: {id} a {nuevo_nombre}")
    else:
        print("ID no encontrado.")

        
def eliminar(id):
    if id in db:
        del db[id]
        print(f"Eliminado: {id}")
    else:
        print("ID no encontrado.")
  
  
if __name__ == "__main__":
    mostrar_menu()