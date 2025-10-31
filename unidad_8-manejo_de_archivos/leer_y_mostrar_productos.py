## EJERCICIO 2: LEER Y MOSTRAR PRODUCTOS ##

# Se utiliza 'with open' para asegurar que el archivo se cierre automáticamente
print("2. Leyendo y mostrando productos en formato ficha:")

try:
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            
            if len(partes) == 3:
                nombre = partes[0].strip()   # Nombre del producto
                precio = partes[1].strip()   # Precio
                cantidad = partes[2].strip() # Cantidad

                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
            else:
                print(f"[error] Linea con formato incorrecto: {linea_limpia}")
                
except FileNotFoundError:
    print("\n[error] El archivo 'archivo.txt' no se encontro ,ejecuta el Ejercicio 1 primero.")

print("Lectura de archivo finalizada\n")