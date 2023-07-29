def imprimir_mapa(mapa):
    # Diccionario de caracteres y colores para representar los tipos de terreno
    caracteres_terreno = {
        "prado": ("\033[92m*\033[0m",),  # Verde
        "hierba": ("\033[32m\"\033[0m",),  # Verde claro
        "casa": ("\033[91m#\033[0m",),  # Rojo
        "colina": ("\033[33m∩\033[0m",),  # Amarillo
        "lago": ("\033[94m~\033[0m",),  # Azul
        "rio": ("\033[96m┬\033[0m",),  # Cyan
        "arena": ("\033[93m∙\033[0m",),  # Amarillo claro
        "costa": ("\033[95m^\033[0m",),  # Magenta
        "mar": ("\033[34m≈\033[0m",),  # Azul claro
        "arbol": ("\033[32m♠\033[0m",),  # Verde claro
    }

    for fila in mapa:
        for terreno in fila:
            caracter = caracteres_terreno.get(terreno, ("\033[90m?\033[0m",))  # Usar "?" en gris si el tipo de terreno no está en el diccionario
            print(*caracter, end=" ")
        print()
