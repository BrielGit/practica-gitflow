# crud.py
db = {}

def mostrar_menu():
    print("\n--- Sistema CRUD ---")
    print("1. Crear | 2. Leer | 3. Actualizar | 4. Eliminar | 5. Salir")

def eliminar(id):
    if id in db:
        del db[id]
        print(f"Eliminado: {id}")
    else:
        print("ID no encontrado.")
        
if __name__ == "__main__":
    mostrar_menu()