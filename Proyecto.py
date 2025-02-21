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


# Función para ver el historial de registros
def ver_historial():
    if not datos:
        print("No hay registros disponibles.\n")
    else:
        print("Historial de Ingresos y Egresos:")
        for item in datos:
            print(f"{item['Fecha']} - {item['Tipo'].capitalize()} - ${item['Monto']} - {item['Descripcion']}")
        print()


