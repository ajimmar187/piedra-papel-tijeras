"""
Piedra, Papel y Tijeras - Versión con Control de Errores
=========================================================
Implementación mejorada con manejo robusto de excepciones personalizadas.

Características:
- Excepciones personalizadas para opciones inválidas
- Manejo de errores con try-except
- Validación de entrada más robusta
- Conversión a minúsculas para mejor UX
"""

import random

# Definición de las acciones del juego
PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'


class OpcionIncorrectaException(Exception):
    """Excepción levantada cuando el usuario elige una opción inválida."""
    pass


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
    """Función principal que ejecuta el bucle del juego con manejo de errores."""
    acciones_juego = [PIEDRA, PAPEL, TIJERAS]
    
    print("=== Bienvenido a Piedra, Papel y Tijeras (v2) ===\n")

    while True:
        try:
            # Obtener entrada del usuario y convertir a minúsculas
            eleccion_usuario = input("\nElige una opción (piedra, papel, tijeras) o escribe 'salir': ").lower()
            
            # Permitir que el usuario salga del juego
            if eleccion_usuario == 'salir':
                print("\n¡Gracias por jugar! Hasta luego.")
                break
            
            # Validar que la entrada sea una opción válida; si no, lanzar excepción
            if eleccion_usuario not in acciones_juego:
                raise OpcionIncorrectaException
            
            # Computadora elige una acción aleatoria
            eleccion_computadora = random.choice(acciones_juego)

            print(f"\nElegiste {eleccion_usuario}. La computadora eligió {eleccion_computadora}")
            evaluar_juego(eleccion_usuario, eleccion_computadora)
            
        except OpcionIncorrectaException:
            # Capturar la excepción de opción inválida y mostrar mensaje de error
            print("\n¡Solo puedes elegir piedra, papel o tijeras!")


if __name__ == "__main__":
    main()
