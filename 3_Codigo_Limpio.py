"""
Piedra, Papel y Tijeras - Versión con Código Limpio
====================================================
Implementación más estructurada utilizando Enums y separación de responsabilidades.

Características:
- Uso de Enums para mejorar legibilidad y mantenibilidad
- Funciones claramente separadas por responsabilidad
- Mejor validación de entrada con manejo de excepciones
- Mensajes formateados dinámicamente
"""

import random
from enum import IntEnum


class AccionJuego(IntEnum):
    """Enum que representa las acciones posibles en el juego."""
    Piedra = 0
    Papel = 1
    Tijeras = 2


def evaluar_juego(eleccion_usuario, eleccion_computadora):
    """
    Determina el resultado del juego y muestra el mensaje correspondiente.
    
    Args:
        eleccion_usuario (AccionJuego): La acción elegida por el usuario
        eleccion_computadora (AccionJuego): La acción elegida por la computadora
    """
    if eleccion_usuario == eleccion_computadora:
        print(f"El usuario y la computadora eligieron {eleccion_usuario.name}. ¡Empate!")

    # Eligiste Piedra
    elif eleccion_usuario == AccionJuego.Piedra:
        if eleccion_computadora == AccionJuego.Tijeras:
            print("La piedra rompe las tijeras. ¡Ganaste!")
        else:
            print("El papel envuelve la piedra. ¡Perdiste!")

    # Eligiste Papel
    elif eleccion_usuario == AccionJuego.Papel:
        if eleccion_computadora == AccionJuego.Piedra:
            print("El papel envuelve la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")

    # Eligiste Tijeras
    elif eleccion_usuario == AccionJuego.Tijeras:
        if eleccion_computadora == AccionJuego.Piedra:
            print("La piedra rompe las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")

            
def obtener_accion_computadora():
    """
    Genera una acción aleatoria para la computadora.
    
    Returns:
        AccionJuego: La acción elegida aleatoriamente por la computadora
    """
    seleccion_computadora = random.randint(0, len(AccionJuego) - 1)
    accion_computadora = AccionJuego(seleccion_computadora)
    print(f"La computadora eligió {accion_computadora.name}.")
    
    return accion_computadora
            

def obtener_accion_usuario():
    """
    Obtiene la acción del usuario mediante entrada, con validación.
    
    Returns:
        AccionJuego: La acción elegida por el usuario
        
    Raises:
        ValueError: Si la entrada no es un número válido dentro del rango
    """
    # Generar dinámicamente el string de opciones desde el Enum
    opciones_juego = [f"{accion_juego.name}[{accion_juego.value}]" for accion_juego in AccionJuego]
    opciones_juego_str = ", ".join(opciones_juego)
    seleccion_usuario = int(input(f"\nElige una opción ({opciones_juego_str}): "))
    accion_usuario = AccionJuego(seleccion_usuario)
       
    return accion_usuario


def jugar_otra_ronda():
    """
    Pregunta al usuario si desea jugar otra ronda.
    
    Returns:
        bool: True si el usuario quiere otra ronda, False en caso contrario
    """
    otra_ronda = input("\n¿Otra ronda? (s/n): ")
    return otra_ronda.lower() == 's'
        

def main():
    """Función principal que ejecuta el bucle del juego."""
    print("=== Bienvenido a Piedra, Papel y Tijeras (v3) ===\n")
    
    while True:
        try:
            eleccion_usuario = obtener_accion_usuario()
        except ValueError:
            # Mostrar el rango válido de opciones
            rango_str = f"[0, {len(AccionJuego) - 1}]"
            print(f"Selección inválida. ¡Elige una opción dentro del rango {rango_str}!")
            continue

        eleccion_computadora = obtener_accion_computadora()
        evaluar_juego(eleccion_usuario, eleccion_computadora)

        if not jugar_otra_ronda():
            print("\n¡Gracias por jugar! Hasta luego.")
            break
        

if __name__ == "__main__":
    main()
