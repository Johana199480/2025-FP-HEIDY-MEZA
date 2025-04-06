# Abrir archivo para escritura
Archivo = open('my_notes.txt', 'w')

# Escribir 3 líneas
Archivo.write('Hoy inicié mi primer día como auxiliar contable.\n')
Archivo.write('Es un nuevo desafío y aunque al inicio me sentí angustiada, me están guiando bien.\n')
Archivo.write('Estoy aprendiendo a utilizar el sistema contable y revisando facturas.\n')

# Cerrar el archivo después de escribir
Archivo.close()

# Abrir archivo para lectura
Archivo = open('my_notes.txt', 'r')

# Indicar que se lee línea a línea y eliminar saltos de línea extras
print(Archivo.readline().strip())
print(Archivo.readline().strip())
print(Archivo.readline().strip())

# Cerrar el archivo
Archivo.close()
