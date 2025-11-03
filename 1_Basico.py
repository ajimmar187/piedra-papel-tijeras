"""
Piedra, Papel y Tijeras - Versión Básica
==========================================
Implementación simple del juego clásico de Piedra, Papel y Tijeras.
El usuario juega contra la computadora en un bucle infinito.

Características:
- Validación básica de entrada
- Lógica de juego simple y directa
"""

import random

# Definición de las acciones del juego
PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'


def evaluar_juego(eleccion_usuario, eleccion_computadora):
    """
    Determina el resultado del juego y muestra el mensaje correspondiente.
    
    Args:
        eleccion_usuario (str): La acción elegida por el usuario
        eleccion_computadora (str): La acción elegida por la computadora
    """
    if eleccion_usuario == eleccion_computadora:
        print(f"El usuario y la computadora eligieron {eleccion_usuario}. ¡Empate!")

    # Eliges Piedra
    elif eleccion_usuario == PIEDRA:
        if eleccion_computadora == TIJERAS:
            print("La piedra rompe las tijeras. ¡Ganaste!")
        else:
            print("El papel envuelve la piedra. ¡Perdiste!")

    # Eliges Papel
    elif eleccion_usuario == PAPEL:
        if eleccion_computadora == PIEDRA:
            print("El papel envuelve la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")

    # Eliges Tijeras
    elif eleccion_usuario == TIJERAS:
        if eleccion_computadora == PIEDRA:
            print("La piedra rompe las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")


def main():
    """Función principal que ejecuta el bucle del juego."""
    acciones_juego = [PIEDRA, PAPEL, TIJERAS]
    
    print("=== Bienvenido a Piedra, Papel y Tijeras ===\n")

    while True:
        # Obtener entrada del usuario (convertida a minúsculas para mayor flexibilidad)
        eleccion_usuario = input("\nElige una opción (piedra, papel, tijeras) o escribe 'salir' para terminar: ").lower()
        
        # Permitir que el usuario salga del juego
        if eleccion_usuario == 'salir':
            print("\n¡Gracias por jugar! Hasta luego.")
            break
        
        # Validar que la entrada sea una opción válida
        if eleccion_usuario not in acciones_juego:
            print("¡Opción inválida! Por favor, elige piedra, papel o tijeras.")
            continue
        
        # Computadora elige una acción aleatoria
        eleccion_computadora = random.choice(acciones_juego)

        print(f"\nElegiste {eleccion_usuario}. La computadora eligió {eleccion_computadora}")
        evaluar_juego(eleccion_usuario, eleccion_computadora)


if __name__ == "__main__":
    main()
