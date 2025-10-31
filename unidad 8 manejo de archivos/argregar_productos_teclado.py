## 3: AGREGAR PRODUCTOS DESDE TECLADO ##

NOMBRE_ARCHIVO = "archivo.txt"

## leer y mostrar productos actuales ##
print("3 agregando productos al archivo:")
print("\n PRODUCTOS ACTUALES ")

try:
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            
            if len(partes) == 3:
                nombre = partes[0].strip()
                precio = partes[1].strip()
                cantidad = partes[2].strip()
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
except FileNotFoundError:
    print(f"[error] El archivo '{NOMBRE_ARCHIVO}' no se encontro ejecuta el Ejercicio 1 primero.")
    exit() # Finaliza el programa si hay error de archivo



## pedir datos al usuario ##
print("Ingrese los datos del nuevo producto:")
nuevo_nombre = input("Nombre del producto: ").strip()
nuevo_precio = input("Precio (ej: 1.500.000): ").strip()
nueva_cantidad = input("Cantidad: ").strip()

## agregar al archivo sin borrar ##

# Construir la nueva línea de texto
nueva_linea = f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n"

try:
    with open(NOMBRE_ARCHIVO, "a") as archivo:
        archivo.write(nueva_linea)
    
    print(f"\n Producto '{nuevo_nombre}' agregado exitosamente a '{NOMBRE_ARCHIVO}'.")

except Exception as e:
    print(f"\n[error] No se pudo escribir en el archivo: {e}")

# comprobación final
print("\n nuevo contenido del archivo (comprobación)")
try:
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        contenido_completo = archivo.read()
        print(contenido_completo.strip())
except:
    pass
print("Fin del programa.")