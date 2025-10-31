## EJERCICIO 5: BUSCAR PRODUCTO POR NOMBRE ##

NOMBRE_ARCHIVO = "archivo.txt"
productos = [] 
producto_encontrado = None 

print("5. Buscando producto por nombre:")
print("Cargando datos del archivo...")
try:
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            
            if len(partes) == 3:
                try:
                    nombre = partes[0].strip()
                    precio = float(partes[1].strip().replace('.', ''))
                    cantidad = int(partes[2].strip())
                    
                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except ValueError:
                    ## Ignorar lineas que no se pueden convertir a nums ##
                    continue 
except FileNotFoundError:
    print(f"[error] El archivo '{NOMBRE_ARCHIVO}' no se encontro No se puede realizar la busqueda.")
    exit()

## pedir nombre a buscar y recorrer la lista ##
nombre_a_buscar = input(" Ingrese el nombre del producto a buscar: ").strip().lower()

## Recorrer la lista de diccionarios ##
for producto in productos:
    ## Comparamos el nombre ingresado con el nombre del producto ##
    if producto["nombre"].lower() == nombre_a_buscar:
        producto_encontrado = producto
        break # Usamos 'break' para detener la busqueda una vez que se encuentra el producto

## 3 mostrar resultado ##

if producto_encontrado:
    ## mostramos sus datos ##
    print("\n Producto encontrado:")
    print(f"   Nombre:   {producto_encontrado['nombre']}")
    ## Formateamos el precio con separador de miles y dos decimales ##
    print(f"   Precio:   ${producto_encontrado['precio']:,.2f}") 
    print(f"   Cantidad: {producto_encontrado['cantidad']}")
else:
    ## No se encontro el producto ##
    print(f"\n error el producto '{nombre_a_buscar.capitalize()}' no se encuentra en el inventario")

print("Búsqueda finalizada.\n")