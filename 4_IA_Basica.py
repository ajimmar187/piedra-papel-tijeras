"""
Piedra, Papel y Tijeras - Versión con IA Básica
================================================
Implementación con una estrategia de IA simple que aprende de sus propios resultados
en rondas anteriores.

Características:
- Enums para acciones y resultados del juego
- Historial de acciones de la IA y resultados para análisis
- IA básica que adapta su estrategia según su propio desempeño anterior
- Manejo robusto de errores

Estrategia de IA JUSTA Y HONESTA:

IMPORTANTE: El historial de resultados (historial_juego) se guarda desde la perspectiva
del usuario:
  - ResultadoJuego.Victoria = el usuario ganó (la IA perdió)
  - ResultadoJuego.Derrota = el usuario perdió (la IA ganó)
  - ResultadoJuego.Empate = fue empate

La lógica de la IA:
1. Primera ronda: elige aleatoriamente (sin información)
2. Si el usuario ganó la última ronda (IA perdió): intenta una acción diferente
3. Si el usuario perdió la última ronda (IA ganó): repite esa acción ganadora
4. Si fue empate: elige aleatoriamente

NOTA IMPORTANTE: La IA NUNCA mira la acción actual que el usuario acaba de elegir.
Solo analiza su propio historial de acciones y los resultados pasados.
Mirar la acción del usuario sería hacer trampa.
"""

import random
from enum import IntEnum


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



def evaluar_juego(eleccion_usuario, eleccion_computadora):
    """
    Determina el resultado del juego y muestra el mensaje correspondiente.
    
    Los resultados se reportan desde la perspectiva del usuario:
    - Victoria: el usuario ganó
    - Derrota: el usuario perdió
    - Empate: fue un empate
    
    Args:
        eleccion_usuario (AccionJuego): La acción elegida por el usuario
        eleccion_computadora (AccionJuego): La acción elegida por la computadora
        
    Returns:
        ResultadoJuego: El resultado del juego para el usuario (Victoria/Derrota/Empate)
    """
    
    if eleccion_usuario == eleccion_computadora:
        print(f"El usuario y la computadora eligieron {eleccion_usuario.name}. ¡Empate!")
        resultado_juego = ResultadoJuego.Empate

    # Elegiste Piedra
    elif eleccion_usuario == AccionJuego.Piedra:
        if eleccion_computadora == AccionJuego.Tijeras:
            print("La piedra rompe las tijeras. ¡Ganaste!")
            resultado_juego = ResultadoJuego.Victoria
        else:  # La computadora eligió Papel
            print("El papel envuelve la piedra. ¡Perdiste!")
            resultado_juego = ResultadoJuego.Derrota

    # Elegiste Papel
    elif eleccion_usuario == AccionJuego.Papel:
        if eleccion_computadora == AccionJuego.Piedra:
            print("El papel envuelve la piedra. ¡Ganaste!")
            resultado_juego = ResultadoJuego.Victoria
        else:  # La computadora eligió Tijeras
            print("Las tijeras cortan el papel. ¡Perdiste!")
            resultado_juego = ResultadoJuego.Derrota

    # Elegiste Tijeras
    else:  # eleccion_usuario == AccionJuego.Tijeras
        if eleccion_computadora == AccionJuego.Piedra:
            print("La piedra rompe las tijeras. ¡Perdiste!")
            resultado_juego = ResultadoJuego.Derrota
        else:  # La computadora eligió Papel
            print("Las tijeras cortan el papel. ¡Ganaste!")
            resultado_juego = ResultadoJuego.Victoria

    return resultado_juego

            
def obtener_accion_computadora(historial_juego, historial_computadora):
    """
    Obtiene la acción de la computadora basada en la IA simple y honesta.
    
    Estrategia HONESTA (no hace trampa):
    - La IA solo consulta su PROPIO historial de acciones anteriores
    - La IA NUNCA mira la acción actual que acaba de elegir el usuario
    - Adapta su estrategia basándose en sus propios resultados pasados
    
    Reglas:
    - Primera ronda: acción aleatoria (sin información)
    - Si el usuario ganó la última ronda (IA perdió): elige una acción diferente
    - Si el usuario perdió la última ronda (IA ganó): repite esa acción ganadora
    - Si fue empate: acción aleatoria
    
    Nota sobre historial_juego: Los resultados se guardan desde la perspectiva del usuario
    (Victoria = el usuario ganó, Derrota = el usuario perdió, Empate = empate)
    
    Args:
        historial_juego (list): Historial de resultados del juego (perspectiva del usuario)
        historial_computadora (list): Historial de PROPIAS acciones de la IA (lo importante)
        
    Returns:
        AccionJuego: La acción elegida por la computadora
    """
    # Primera ronda sin historial => elección aleatoria
    if len(historial_computadora) == 0:
        accion_computadora = obtener_accion_aleatoria_computadora()
    else:
        # Analizar el resultado de la última ronda (desde la perspectiva del usuario)
        ultimo_resultado = historial_juego[-1]
        
        # Si el usuario ganó (IA perdió): intentar una acción diferente de la que perdió
        if ultimo_resultado == ResultadoJuego.Victoria:
            # La acción anterior de la IA fue la que perdió contra el usuario, hay que cambiar
            accion_que_perdio = historial_computadora[-1]
            acciones_disponibles = [a for a in AccionJuego if a != accion_que_perdio]
            # Elegir aleatoriamente de las dos opciones restantes
            accion_computadora = random.choice(acciones_disponibles)
        
        # Si el usuario perdió (IA ganó): mantener la estrategia ganadora
        elif ultimo_resultado == ResultadoJuego.Derrota:
            # La IA repite su última acción porque venció al usuario
            accion_computadora = historial_computadora[-1]
        
        # Si fue empate: elección aleatoria
        else:
            accion_computadora = obtener_accion_aleatoria_computadora()
    
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


def jugar_otra_ronda():
    """
    Pregunta al usuario si desea jugar otra ronda.
    
    Returns:
        bool: True si el usuario quiere otra ronda, False en caso contrario
    """
    otra_ronda = input("\n¿Otra ronda? (s/n): ")
    return otra_ronda.lower() == 's'
        

def main():
    """Función principal que ejecuta el bucle del juego con IA básica."""
    print("=== Bienvenido a Piedra, Papel y Tijeras (v4 - IA Básica) ===\n")
    
    historial_juego = []
    historial_acciones_usuario = []
    historial_acciones_computadora = []
    
    while True:
        try:
            eleccion_usuario = obtener_accion_usuario()
            historial_acciones_usuario.append(eleccion_usuario)
        except ValueError:
            rango_str = f"[0, {len(AccionJuego) - 1}]"
            print(f"Selección inválida. ¡Elige una opción dentro del rango {rango_str}!")
            continue

        eleccion_computadora = obtener_accion_computadora( historial_juego, historial_acciones_computadora)
        historial_acciones_computadora.append(eleccion_computadora)
        resultado_juego = evaluar_juego(eleccion_usuario, eleccion_computadora)
        historial_juego.append(resultado_juego)

        if not jugar_otra_ronda():
            print("\n¡Gracias por jugar! Hasta luego.")
            break
        

if __name__ == "__main__":
    main()
