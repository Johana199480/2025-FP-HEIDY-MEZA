# Función para calcular el promedio de temperaturas por ciudad
def calcular_promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio por ciudad.

    :param datos: Lista de diccionarios con datos de temperatura por ciudad y semanas.
    :return: Diccionario con el promedio de temperatura por ciudad.
    """
    promedios = {}

    for ciudad in datos:
        total_temp = 0
        total_dias = 0

        for semana in ciudad["semanas"]:
            for dia in semana:
                total_temp += dia["temp"]
                total_dias += 1

        promedio = total_temp / total_dias
        promedios[ciudad["ciudad"]] = round(promedio, 2)

    return promedios

# Datos de temperaturas
temperaturas = [
    {
        "ciudad": "Azuay",
        "semanas": [
            [
                {"day": "Lunes", "temp": 15},
                {"day": "Martes", "temp": 14},
                {"day": "Miércoles", "temp": 16},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 13},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 14}
            ],
            [
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 15},
                {"day": "Miércoles", "temp": 14},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 18},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 13}
            ]
        ]
    },
    {
        "ciudad": "Loja",
        "semanas": [
            [
                {"day": "Lunes", "temp": 14},
                {"day": "Martes", "temp": 16},
                {"day": "Miércoles", "temp": 15},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 13},
                {"day": "Sábado", "temp": 14},
                {"day": "Domingo", "temp": 16}
            ],
            [
                {"day": "Lunes", "temp": 15},
                {"day": "Martes", "temp": 13},
                {"day": "Miércoles", "temp": 16},
                {"day": "Jueves", "temp": 14},
                {"day": "Viernes", "temp": 17},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 14}
            ]
        ]
    },
    # Agregar los datos de la ciudad Manabí
    {
        "ciudad": "Manabí",
        "semanas": [
            [  # Semana 1
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 14},
                {"day": "Miércoles", "temp": 15},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 18},
                {"day": "Sábado", "temp": 16},
                {"day": "Domingo", "temp": 14},
            ],
            [  # Semana 2
                {"day": "Lunes", "temp": 17},
                {"day": "Martes", "temp": 15},
                {"day": "Miércoles", "temp": 16},
                {"day": "Jueves", "temp": 14},
                {"day": "Viernes", "temp": 17},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 13},
            ],
            [  # Semana 3
                {"day": "Lunes", "temp": 15},
                {"day": "Martes", "temp": 16},
                {"day": "Miércoles", "temp": 14},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 15},
                {"day": "Sábado", "temp": 14},
                {"day": "Domingo", "temp": 16},
            ],
            [  # Semana 4
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 17},
                {"day": "Miércoles", "temp": 15},
                {"day": "Jueves", "temp": 18},
                {"day": "Viernes", "temp": 19},
                {"day": "Sábado", "temp": 16},
                {"day": "Domingo", "temp": 17},
            ]
        ]
    }
]

# Calcular el promedio de las temperaturas para cada ciudad
resultados_promedios = calcular_promedio_temperaturas(temperaturas)

# Mostrar los promedios por ciudad
for ciudad_nombre, promedio_temperatura in resultados_promedios.items():
    print(f"Ciudad: {ciudad_nombre} - Promedio de temperatura: {promedio_temperatura}°C")


