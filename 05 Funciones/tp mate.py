#trabajo integrador de matematica
# crear un programa que contenga las operaciones con los DNI

dni_list = []
while True:
    dni = input("Ingrese un DNI (o 'salir' para terminar): ")
    if dni.lower() == 'salir':
        break
    elif dni.isdigit() and len(dni) == 8:
        if int(dni) > 10000000 and int(dni) < 50000000:
            dni_list.append(dni)
            print("DNI agregado correctamente.")
        else:
            print("DNI fuera de rango. Debe ser mayor a 10.000.000 y menor a 50.000.000.")
    else:
        print("DNI inválido. Por favor, ingrese un número de 8 dígitos.")

print("\nDNI ingresados:")
for i, dni in enumerate(dni_list):
    print(f"{i+1}. {dni}")

