# contador_palabras.py

import re
from collections import Counter

def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.
    """
    # Usamos expresiones regulares para encontrar solo palabras y convertirlas a minúsculas
    palabras = re.findall(r'\b\w+\b', texto.lower())
    frecuencia = Counter(palabras)
    return frecuencia

if __name__ == "__main__":
    print("--- Contador de Frecuencia de Palabras ---")
    texto_usuario = input("Ingresa el texto que quieres analizar:\n> ")

    if not texto_usuario.strip():
        print("\nNo se ingresó ningún texto.")
    else:
        frecuencia_palabras = contar_palabras(texto_usuario)
        print("\n--- Frecuencia de cada palabra ---")
        for palabra, conteo in frecuencia_palabras.items():
            print(f"'{palabra}': {conteo}")