# Crear un diccionario con información ficticia sobre una persona
informacion_personal = {
    "nombre": "Leonel Jaramillo",
    "edad": 25,
    "ciudad": "Manta",  # Ciudad de origen
    "profesion": "Artes escénicas"
}

# Guardar la ciudad de origen
ciudad_origen = informacion_personal["ciudad"]

# Modificar la ciudad
informacion_personal["ciudad"] = "Ibarra"
ciudad_modificada = informacion_personal["ciudad"]

# Agregar una nueva clave-valor que represente el "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0967132349"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir los resultados
print(f"Ciudad de origen: {ciudad_origen}")
print(f"Ciudad modificada: {ciudad_modificada}")
print("Diccionario final:", informacion_personal)
