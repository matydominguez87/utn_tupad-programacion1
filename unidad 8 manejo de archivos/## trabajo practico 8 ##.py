## trabajo practico 8 ##


NOMBRE_ARCHIVO = "productos_simple.txt"
productos = [] 


## 1. CREAR ARCHIVO (w) ##

print(" 1. Creando archivo de datos iniciales ")
try:
    archivo = open(NOMBRE_ARCHIVO, "w")
    archivo.write("bicicleta,200000,23\n")
    archivo.write("moto,5400000,12\n")
    archivo.write("auto,15000000,5\n")
    archivo.close()
    print(" creaste el archivo\n")
except:
    print(" error al crear el archivo.\n")



## 4 CARGAR PRODUCTOS EN LISTA DE DICCIONARIOS (r) ##
# lo hago antes del 2 para tener la lista de productos

print("4. Cargando datos del archivo a una lista de diccionarios ")
try:
    archivo = open(NOMBRE_ARCHIVO, "r")
    
    for linea in archivo:
        linea_limpia = linea.strip() ## saco el salto de linea ##
        partes = linea_limpia.split(",") ## Separo por coma ##
        
        ## Asumo que siempre hay 3 partes ##
        nombre = partes[0].strip()
        precio = partes[1].strip()
        cantidad = partes[2].strip()
        
        ## Creo el diccionario ##
        producto_dic = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad 
        }
        
        ## añado el diccio a la lista ##
        productos.append(producto_dic)
        
    archivo.close()
    print(" ya cargaste los datos en la lista  'productos' genio \n")
except FileNotFoundError:
    print(" le erraste , no encuentro el archivo")


## 2 LEER Y MOSTRAR PRODUCTOS ##
print(" 2. Mostrando productos  ##")
for p in productos:
    # Muestro los datos de la lista de diccionarios
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")    


## 3. AGREGAR PRODUCTOS DESDE TECLADO ('a') ##
print("\n## 3. metiendo  un nuevo producto al archivo :) ##")

## Pedir datos ##
nuevo_nombre = input(" metele el nombre del nuevo producto: ").strip()
nuevo_precio = input("mandale el precio: ").strip()
nueva_cantidad = input("cuantos tenes ?: ").strip()

## Formato de la línea ##
nueva_linea = f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n"

## Escribir en el archivo en modo 'a' ##
try:
    archivo = open(NOMBRE_ARCHIVO, "a")
    archivo.write(nueva_linea)
    archivo.close()
    print(f" Producto '{nuevo_nombre}' agregado al archivo '{NOMBRE_ARCHIVO}'.")
except:
    print(" le erraste al agregar el producto genio.")




## 5. BUSCAR PRODUCTO POR NOMBRE  ##
print("\n 5. Buscando producto por nombre ##")

nombre_a_buscar = input("mandale el nombre de un producto que te lo busco: ").strip().lower()

producto_encontrado = None

## Recorrer la lista de diccionarios ##
for p in productos:
    if p["nombre"].lower() == nombre_a_buscar:
        producto_encontrado = p
        break ## freno la busqueda al encontrarlo ##

if producto_encontrado:
    print("\n Producto encontrado:")
    print(f"   Nombre:   {producto_encontrado['nombre']}")
    print(f"   Precio:   ${producto_encontrado['precio']}")
    print(f"   Cantidad: {producto_encontrado['cantidad']}")
else:
    print(f"\n le erraste master  El producto '{nombre_a_buscar.capitalize()}' no esta en la lista.")


## 6. GUARDAR PRODUCTOS ACTUALIZADOS (w) ##
print("\n 6. Sobrescribiendo el archivo con datos actualizados ")
productos_actualizados = [] ## nueva lista ##

try:
    archivo = open(NOMBRE_ARCHIVO, "r")
    for linea in archivo:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(",")
        productos_actualizados.append({
            "nombre": partes[0].strip(),
            "precio": partes[1].strip(),
            "cantidad": partes[2].strip()
        })
    archivo.close()
except:
    print(" Error al recargar la lista.")

try:
    ## w borra el contenido y escribe desde cero ##
    archivo = open(NOMBRE_ARCHIVO, "w")
    for p in productos_actualizados:
        linea_a_escribir = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea_a_escribir)
        
    archivo.close()
    print(f" Archivo '{NOMBRE_ARCHIVO}' sobrescrito con {len(productos_actualizados)} productos (incluyendo el nuevo).")
    print("Contenido final del archivo:")
   ## comprobacion final ##
    archivo = open(NOMBRE_ARCHIVO, "r")
    print(archivo.read())
    archivo.close()
    
except:
    print("error al sobrescribir el archivo.")

