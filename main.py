import mapa
import visualizacion

def obtener_tamano_mapa():
    # Solicitar al usuario el ancho y alto del mapa
    try:
        width = int(input("Ingresa el ancho del mapa en tiles: "))
        height = int(input("Ingresa el alto del mapa en tiles: "))
        return width, height
    except ValueError:
        print("Error: Por favor ingresa valores enteros válidos.")
        return obtener_tamano_mapa()

def obtener_bioma():
    # Mostrar la lista de biomas disponibles
    print("Biomas disponibles:")
    for i, bioma in enumerate(mapa.BIOMAS.keys(), start=1):
        print(f"{i}. {bioma}")

    # Solicitar al usuario que elija un bioma
    opcion = 0
    while opcion < 1 or opcion > len(mapa.BIOMAS):
        try:
            opcion = int(input("Elige un bioma (número): "))
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

    biomas = list(mapa.BIOMAS.keys())
    return biomas[opcion - 1]

def main():
    # Solicitar al usuario el tamaño del mapa
    width, height = obtener_tamano_mapa()

    # Solicitar al usuario que elija un bioma
    bioma = obtener_bioma()

    # Generar el mapa
    mapa_generado = mapa.generar_mapa_coherente(width, height, bioma)

    # Visualizar el mapa
    visualizacion.imprimir_mapa(mapa_generado)

if __name__ == "__main__":
    main()
