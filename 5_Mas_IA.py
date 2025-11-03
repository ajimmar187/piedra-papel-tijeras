"""
Piedra, Papel y Tijeras - Versión con IA Avanzada
==================================================
Implementación con una estrategia de IA más sofisticada que analiza 
los patrones recientes de las acciones del usuario.

Características:
- Enums para acciones y resultados del juego
- Historial de acciones para análisis de patrones
- IA avanzada que detecta la acción más frecuente reciente del usuario
- Análisis estadístico de movimientos recientes

Estrategia de IA:
- Detecta los últimos N movimientos del usuario
- Calcula cuál es la acción más frecuente en esos movimientos
- Elige la acción que vence esa opción más frecuente
"""

import random
from enum import IntEnum
from statistics import mode


class AccionJuego(IntEnum):
    """Enum que representa las acciones posibles en el juego."""
    Piedra = 0
    Papel = 1
    Tijeras = 2


class ResultadoJuego(IntEnum):
    """Enum que representa los posibles resultados del juego."""
    Victoria = 0
    Derrota = 1
    Empate = 2


# Diccionario que define qué acción vence a otra
Victorias = {
    AccionJuego.Piedra: AccionJuego.Papel,    # Papel vence a Piedra
    AccionJuego.Papel: AccionJuego.Tijeras,   # Tijeras vence a Papel
    AccionJuego.Tijeras: AccionJuego.Piedra   # Piedra vence a Tijeras
}

# Número de acciones recientes a analizar para detectar patrones
NUMERO_ACCIONES_RECIENTES = 5


def evaluar_juego(eleccion_usuario, eleccion_computadora):
    """
    Determina el resultado del juego y muestra el mensaje correspondiente.
    
    Args:
        eleccion_usuario (AccionJuego): La acción elegida por el usuario
        eleccion_computadora (AccionJuego): La acción elegida por la computadora
        
    Returns:
        ResultadoJuego: El resultado del juego para el usuario
    """
    
    if eleccion_usuario == eleccion_computadora:
        print(f"El usuario y la computadora eligieron {eleccion_usuario.name}. ¡Empate!")
        resultado_juego = ResultadoJuego.Empate

    # Elegiste Piedra
    elif eleccion_usuario == AccionJuego.Piedra:
        if eleccion_computadora == AccionJuego.Tijeras:
            print("La piedra rompe las tijeras. ¡Ganaste!")
            resultado_juego = ResultadoJuego.Victoria
        else:
            print("El papel envuelve la piedra. ¡Perdiste!")
            resultado_juego = ResultadoJuego.Derrota

    # Elegiste Papel
    elif eleccion_usuario == AccionJuego.Papel:
        if eleccion_computadora == AccionJuego.Piedra:
            print("El papel envuelve la piedra. ¡Ganaste!")
            resultado_juego = ResultadoJuego.Victoria
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")
            resultado_juego = ResultadoJuego.Derrota

    # Elegiste Tijeras
    elif eleccion_usuario == AccionJuego.Tijeras:
        if eleccion_computadora == AccionJuego.Piedra:
            print("La piedra rompe las tijeras. ¡Perdiste!")
            resultado_juego = ResultadoJuego.Derrota
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")
            resultado_juego = ResultadoJuego.Victoria

    return resultado_juego

            
def obtener_accion_computadora(historial_usuario, historial_juego):
    """
    Obtiene la acción de la computadora basada en análisis de patrones.
    
    Analiza los últimos NUMERO_ACCIONES_RECIENTES movimientos del usuario
    para detectar patrones y elige la acción que vence la opción más frecuente.
    
    Args:
        historial_usuario (list): Historial de acciones del usuario
        historial_juego (list): Historial de resultados del juego
        
    Returns:
        AccionJuego: La acción elegida por la computadora
    """
    # No hay acciones previas del usuario => elección aleatoria de la computadora
    if not historial_usuario or not historial_juego:
        accion_computadora = obtener_accion_aleatoria_computadora()
    # IA avanzada: analizar patrones recientes
    else:
        # Obtener los últimos movimientos del usuario
        acciones_recientes = historial_usuario[-NUMERO_ACCIONES_RECIENTES:]
        # Calcular la acción más frecuente en los movimientos recientes
        accion_mas_frecuente_reciente_usuario = AccionJuego(mode(acciones_recientes))
        # Elegir la acción que vence esa opción más frecuente
        accion_computadora = obtener_accion_ganadora(accion_mas_frecuente_reciente_usuario)

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


def obtener_accion_aleatoria_computadora():
    """
    Genera una acción aleatoria para la computadora.
    
    Returns:
        AccionJuego: Una acción aleatoria
    """
    seleccion_computadora = random.randint(0, len(AccionJuego) - 1)
    accion_computadora = AccionJuego(seleccion_computadora)

    return accion_computadora


def obtener_accion_ganadora(accion_juego):
    """
    Obtiene la acción que vence a la acción dada.
    
    Args:
        accion_juego (AccionJuego): La acción contra la que queremos ganar
        
    Returns:
        AccionJuego: La acción ganadora
    """
    return Victorias[accion_juego]


def jugar_otra_ronda():
    """
    Pregunta al usuario si desea jugar otra ronda.
    
    Returns:
        bool: True si el usuario quiere otra ronda, False en caso contrario
    """
    otra_ronda = input("\n¿Otra ronda? (s/n): ")
    return otra_ronda.lower() == 's'
        

def main():
    """Función principal que ejecuta el bucle del juego con IA avanzada."""
    print("=== Bienvenido a Piedra, Papel y Tijeras (v5 - IA Avanzada) ===\n")
    
    historial_juego = []
    historial_acciones_usuario = []
    
    while True:
        try:
            eleccion_usuario = obtener_accion_usuario()
            historial_acciones_usuario.append(eleccion_usuario)
        except ValueError:
            rango_str = f"[0, {len(AccionJuego) - 1}]"
            print(f"Selección inválida. ¡Elige una opción dentro del rango {rango_str}!")
            continue

        eleccion_computadora = obtener_accion_computadora(historial_acciones_usuario, historial_juego)
        resultado_juego = evaluar_juego(eleccion_usuario, eleccion_computadora)
        historial_juego.append(resultado_juego)

        if not jugar_otra_ronda():
            print("\n¡Gracias por jugar! Hasta luego.")
            break
        

if __name__ == "__main__":
    main()
