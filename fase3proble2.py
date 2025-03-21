# Nombre del estudiante: Luis Navarro Masson
# Grupo: 81
# Número y Texto del programa: Problema 2 - Divisores de un número entre 10 y 90
# Código Fuente: autoría propia

# Inicio del programa
print("Bienvenido. Este programa solicita un número entre 10 y 90 y muestra sus divisores.")

# Validación de entrada
while True:
    try:
        numero = int(input("Por favor, ingrese un número entero entre 10 y 90: "))
        if 10 <= numero <= 90:
            break
        else:
            print("Error: El número debe estar entre 10 y 90. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Debe ingresar un número entero. Inténtelo de nuevo.")

# Cálculo de divisores
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Mostrar resultados
print(f"\nLos divisores del número {numero} son:")
for d in divisores:
    print(f"- {d}")

print(f"\nCantidad total de divisores: {len(divisores)}")
