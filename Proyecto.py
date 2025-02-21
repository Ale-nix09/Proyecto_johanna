#30. Control de Ingresos y Egresos

##🔹Descripción:Un programa para gestionar el dinero de una persona o negocio.

##🔹Requisitos:

#✅ Permitir registrar ingresos y egresos con fecha y descripción.

#✅ Mostrar el saldo actual.

#✅ Mostrar un resumen de ingresos y egresos del mes.

#🔹 Menú:

#1. Registrar ingreso/egreso.
#2. Ver saldo actual.
#3. Ver historial.
#4. Salir.

# Lista para almacenar los datos
datos = []

# Función para registrar ingresos y egresos de manera secuencial
def registrar():
    print("¡Bienvenido al programa de Control de Ingresos y Egresos!")
    print("Vamos a registrar una transacción.")

    # Preguntas en secuencia
    tipo = input("¿Es un ingreso o egreso? (ingreso/egreso): ").lower()
    while tipo not in ['ingreso', 'egreso']:
        print("Opción no válida. Por favor, ingresa 'ingreso' o 'egreso'.")
        tipo = input("¿Es un ingreso o egreso? (ingreso/egreso): ").lower()

    monto = float(input("Monto: "))
    descripcion = input("Descripción: ")
    fecha = input("Fecha (YYYY-MM-DD): ")

    # Guardar los datos en la lista
    datos.append({"Fecha": fecha, "Tipo": tipo, "Monto": monto, "Descripcion": descripcion})
    print("Registro guardado con éxito.\n")

# Función para ver el saldo actual
def ver_saldo():
    saldo = sum(item['Monto'] if item['Tipo'] == 'ingreso' else -item['Monto'] for item in datos)
    print(f"Saldo actual: ${saldo:.2f}\n")

# Función para ver el historial de registros
def ver_historial():
    if not datos:
        print("No hay registros disponibles.\n")
    else:
        print("Historial de Ingresos y Egresos:")
        for item in datos:
            print(f"{item['Fecha']} - {item['Tipo'].capitalize()} - ${item['Monto']} - {item['Descripcion']}")
        print()

# Función para generar la pirámide de asteriscos
def piramide_asteriscos():
    n = int(input("Ingresa el número de filas para la pirámide (mínimo 2): "))
    while n < 2:
        print("Por favor, ingresa un número mayor o igual a 2.")
        n = int(input("Ingresa el número de filas para la pirámide (mínimo 2): "))

    for i in range(1, n + 1):
        espacios = " " * (n - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

# Función para mostrar el menú y ejecutar las opciones
def mostrar_menu():
    print("¡Bienvenido al programa de Control de Ingresos y Egresos!")
    
    while True:
        # Preguntar opción de forma secuencial después de cada acción
        print("\nMenú:")
        print("1. Registrar ingreso/egreso")
        print("2. Ver saldo actual")
        print("3. Ver historial")
        print("4. Salir")
        print("Escribe 'hard' para generar una pirámide de asteriscos.")
        
        opcion = input("Selecciona una opción (1/2/3/4): ").lower()
        
        if opcion == '1':
            registrar()
        elif opcion == '2':
            ver_saldo()
        elif opcion == '3':
            ver_historial()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif opcion == 'hard':
            piramide_asteriscos()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.\n")

# Ejecutar el menú
mostrar_menu()
