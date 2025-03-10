#Creacion de una matriz 3D para almacemar los datos de las temperaturas
#Primera dimensión: Cuidades(Azuay,Loja,Manabí)
#Segunda dimensión: Días de la semana (7 días)
#Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    {
        # Ciudad: Azuay
        "ciudad": "Azuay",
        "semanas": [
            [  # Semana 1
                {"day": "Lunes", "temp": 15},
                {"day": "Martes", "temp": 14},
                {"day": "Miércoles", "temp": 16},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 13},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 14},
            ],
            [  # Semana 2
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 15},
                {"day": "Miércoles", "temp": 14},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 18},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 13},
            ],
            [  # Semana 3
                {"day": "Lunes", "temp": 15},
                {"day": "Martes", "temp": 14},
                {"day": "Miércoles", "temp": 13},
                {"day": "Jueves", "temp": 16},
                {"day": "Viernes", "temp": 17},
                {"day": "Sábado", "temp": 14},
                {"day": "Domingo", "temp": 15},
            ],
            [  # Semana 4
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 17},
                {"day": "Miércoles", "temp": 18},
                {"day": "Jueves", "temp": 19},
                {"day": "Viernes", "temp": 20},
                {"day": "Sábado", "temp": 17},
                {"day": "Domingo", "temp": 16},
            ]
        ]
    },
    {  # Ciudad: Loja
        "ciudad": "Loja",
        "semanas": [
            [  # Semana 1
                {"day": "Lunes", "temp": 14},
                {"day": "Martes", "temp": 16},
                {"day": "Miércoles", "temp": 15},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 13},
                {"day": "Sábado", "temp": 14},
                {"day": "Domingo", "temp": 16},
            ],
            [  # Semana 2
                {"day": "Lunes", "temp": 15},
                {"day": "Martes", "temp": 13},
                {"day": "Miércoles", "temp": 16},
                {"day": "Jueves", "temp": 14},
                {"day": "Viernes", "temp": 17},
                {"day": "Sábado", "temp": 15},
                {"day": "Domingo", "temp": 14},
            ],
            [  # Semana 3
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 14},
                {"day": "Miércoles", "temp": 15},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 13},
                {"day": "Sábado", "temp": 14},
                {"day": "Domingo", "temp": 16},
            ],
            [  # Semana 4
                {"day": "Lunes", "temp": 17},
                {"day": "Martes", "temp": 16},
                {"day": "Miércoles", "temp": 15},
                {"day": "Jueves", "temp": 18},
                {"day": "Viernes", "temp": 19},
                {"day": "Sábado", "temp": 16},
                {"day": "Domingo", "temp": 14},
            ]
        ]
    },
    {  # Ciudad: Manabí
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
# Calcular el promedio de las temperaturas para cada cuidad y semana
for ciudad in temperaturas:
    print(f"Ciudad: {ciudad['ciudad']}")
    for i, semana in enumerate(ciudad['semanas']):
        suma_temperaturas = 0
        for dia in semana:
            suma_temperaturas += dia['temp']
        promedio = suma_temperaturas / len(semana)
        print(f"  Promedio Semana {i + 1}: {promedio:.2f}°C")




