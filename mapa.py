import random

BIOMAS = {
    "Rural": {"prado": 0.4, "hierba": 0.3, "casa": 0.05, "colina": 0.1, "lago": 0.05, "rio": 0.05, "arena": 0.02, "costa": 0.02, "mar": 0.01, "arbol": 0.0},
    "Pradera": {"prado": 0.2, "hierba": 0.4, "casa": 0.01, "colina": 0.2, "lago": 0.05, "rio": 0.05, "arena": 0.02, "costa": 0.02, "mar": 0.01, "arbol": 0.05},
    "Montaña": {"prado": 0.1, "hierba": 0.1, "casa": 0.01, "colina": 0.4, "lago": 0.05, "rio": 0.05, "arena": 0.02, "costa": 0.02, "mar": 0.01, "arbol": 0.2},
    "Cueva": {"prado": 0.1, "hierba": 0.1, "casa": 0.0, "colina": 0.2, "lago": 0.0, "rio": 0.0, "arena": 0.0, "costa": 0.0, "mar": 0.0, "arbol": 0.6},
    "Acantilado": {"prado": 0.05, "hierba": 0.05, "casa": 0.0, "colina": 0.6, "lago": 0.0, "rio": 0.0, "arena": 0.1, "costa": 0.2, "mar": 0.0, "arbol": 0.0},
    "Playa": {"prado": 0.05, "hierba": 0.05, "casa": 0.0, "colina": 0.1, "lago": 0.0, "rio": 0.0, "arena": 0.5, "costa": 0.3, "mar": 0.0, "arbol": 0.0},
    "Bosque": {"prado": 0.1, "hierba": 0.2, "casa": 0.01, "colina": 0.2, "lago": 0.05, "rio": 0.02, "arena": 0.02, "costa": 0.02, "mar": 0.01, "arbol": 0.34},
    "Mar": {"prado": 0.0, "hierba": 0.0, "casa": 0.0, "colina": 0.0, "lago": 0.0, "rio": 0.0, "arena": 0.0, "costa": 0.0, "mar": 1.0, "arbol": 0.0},
    "Pueblo": {"prado": 0.05, "hierba": 0.05, "casa": 0.4, "colina": 0.2, "lago": 0.0, "rio": 0.0, "arena": 0.0, "costa": 0.0, "mar": 0.0, "arbol": 0.3},
}

def obtener_tipo_terreno_coherente(terrenos_vecinos, bioma):
    # Obtener las probabilidades del bioma seleccionado
    probabilidades = BIOMAS[bioma]

    # Calcular la suma total de probabilidades
    suma_probabilidades = sum(probabilidades.values())

    # Ajustar las probabilidades para que sumen 1.0
    probabilidades_ajustadas = {terreno: prob / suma_probabilidades for terreno, prob in probabilidades.items()}

    # Usar las probabilidades ajustadas para obtener el tipo de terreno coherente
    return random.choices(terrenos_vecinos, weights=[probabilidades_ajustadas[terreno] for terreno in terrenos_vecinos])[0]

def generar_mapa_coherente(width, height, bioma):
    mapa = []

    # Inicializar el mapa con tipos de terreno aleatorios
    for _ in range(height):
        fila = [random.choice(list(BIOMAS[bioma].keys())) for _ in range(width)]
        mapa.append(fila)

    for y in range(height):
        for x in range(width):
            # Obtener los tipos de terrenos de los vecinos del tile actual
            terrenos_vecinos = []

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:  # Evitar el tile actual
                        continue

                    vecino_x, vecino_y = x + dx, y + dy

                    if 0 <= vecino_x < width and 0 <= vecino_y < height:
                        terrenos_vecinos.append(mapa[vecino_y][vecino_x])

            tipo_terreno = obtener_tipo_terreno_coherente(terrenos_vecinos, bioma)
            mapa[y][x] = tipo_terreno

    return mapa