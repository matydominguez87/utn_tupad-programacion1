## 4: CARGAR PRODUCTOS EN UNA LISTA DE DICCIONARIOS ##

NOMBRE_ARCHIVO = "archivo.txt"
## lista vacia que almacenara todos nuestros diccionarios
productos = [] 

print("4. Cargando productos desde el archivo a una lista de diccionarios:")

try:
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            
            if len(partes) == 3:
                nombre = partes[0].strip()
                precio_str = partes[1].strip().replace('.', '') ## eliminamos puntos de miles##
                cantidad_str = partes[2].strip()

                try:
                    
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                except ValueError:
                    print(f" No se pudo convertir a numero: {linea_limpia}. Omitiendo registro.")
                    continue # Saltar a la siguiente línea si hay un error de conversion ##

                ## Creamos el diccionario para el producto ##
                producto_diccionario = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }

                ## Agregamos el diccionario a la lista productos ##
                productos.append(producto_diccionario)
            
            else:
                print(f"[error] Línea con formato incorrecto, no cargada: {linea_limpia}")
                
except FileNotFoundError:
    print(f"[error] El archivo '{NOMBRE_ARCHIVO}' no fue encontrado.")

print("\n Lista de diccionarios 'productos' cargada con éxito:")

for p in productos:
    print(f"-> Nombre: {p['nombre']}, Precio: ${p['precio']:,.2f}, Cantidad: {p['cantidad']} (Tipo: {type(p)})")
    
print("\n Contenido de la variable 'productos' (Estructura de datos)")
print(productos)
