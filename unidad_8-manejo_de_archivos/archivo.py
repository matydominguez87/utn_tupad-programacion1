## 1 CREAR ARCHIVO ##
print("1. Escribiendo archivo")
archivo = open("archivo.txt", "w")
archivo.write("bicicleta ,200.000, 23\n")
archivo.write("moto ,5.400.000, 12\n")
archivo.write("auto ,15.000.000, 5\n")
archivo.close()
print("Archivo creado\n")
