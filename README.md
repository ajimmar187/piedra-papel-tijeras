# Piedra, Papel y Tijeras - Progresión de Complejidad

## Introducción

Este proyecto presenta una serie de implementaciones del juego Piedra, Papel y Tijeras, progresando desde lo más básico hasta estrategias de Inteligencia Artificial más sofisticadas. Cada versión introduce nuevos conceptos de programación y patrones de desarrollo.

## Prerrequisitos

Antes de descargar y ejecutar el proyecto, asegúrese de tener instalado Python y uv en su sistema.

### Instalación de Python

- Versión requerida: Python 3.8 o superior
- Descargue Python desde: https://www.python.org/downloads/
- Durante la instalación, marque la opción "Add Python to PATH"

### Instalación de uv

uv es un gestor de paquetes y entorno rápido escrito en Rust. Para instalarlo:

#### En Windows (PowerShell):
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

#### En macOS o Linux (bash/zsh):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Verificar la instalación:
```bash
uv --version
```

## Descarga del Proyecto

### Opción 1: Clonar el repositorio Git
```bash
git clone https://github.com/ajimmar187/piedra-papel-tijeras
cd piedra-papel-tijeras
```

### Opción 2: Descargar manualmente
1. Descargue el archivo ZIP del proyecto
2. Descomprímalo en una carpeta de su preferencia
3. Abra una terminal en esa carpeta

## Configuración del Entorno

### Instalar dependencias

Una vez que haya descargado o clonado el proyecto, navegue a la carpeta del proyecto en la terminal e instale las dependencias usando `uv sync`:

```bash
uv sync
```

Este comando crea automáticamente un entorno virtual en el directorio `.venv` e instala todas las dependencias especificadas en `pyproject.toml`, asegurando que todas las versiones sean compatibles.

El entorno virtual se activa automáticamente cuando ejecuta comandos con `uv run`.

### Activar el entorno virtual manualmente (opcional)

Si prefiere activar el entorno virtual de forma manual para trabajar con él directamente:

**En Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**En Windows (Símbolo del sistema):**
```cmd
.venv\Scripts\activate.bat
```

**En macOS/Linux:**
```bash
source .venv/bin/activate
```

Una vez activado, puede ejecutar los scripts directamente con `python` sin usar `uv run`.

## Estructura del Proyecto

El proyecto contiene 5 versiones del juego, cada una implementando conceptos progresivamente más complejos:

### 1_Basico.py - Implementación Básica

**Nivel:** Fundamentos de programación

**Concepto central:** Este archivo introduce los conceptos elementales de programación necesarios para desarrollar un juego simple.

**Características principales:**
- Implementación simple y directa del juego
- Uso de strings para representar las acciones del juego
- Estructura lógica con condicionales if-elif
- Validación básica de entrada del usuario
- Opción para salir del programa

**Conceptos de programación cubiertos:**
- Variables y constantes
- Definición y llamada de funciones
- Bucles while
- Entrada y salida de datos
- Condicionales (if-elif-else)
- Introducción a listas

**Funciones principales:**
- `evaluar_juego()`: Determina el resultado comparando las acciones
- `main()`: Ejecuta el bucle principal del juego

---

### 2_Control_Errores.py - Manejo de Excepciones

**Nivel:** Intermedio

**Concepto central:** Introducción al manejo robusto de errores mediante excepciones personalizadas.

**Características principales:**
- Definición de excepción personalizada `OpcionIncorrectaException`
- Captura y manejo de excepciones con bloques try-except
- Validación más rigurosa de entrada del usuario
- Conversión automática a minúsculas para mejorar la experiencia del usuario
- Manejo de errores con mensajes informativos

**Conceptos de programación cubiertos:**
- Excepciones personalizadas
- Bloques try-except-finally
- Validación y sanitización de entrada
- Mejora de la robustez del programa

**Funciones principales:**
- `evaluar_juego()`: Determina el resultado del juego
- `main()`: Ejecuta el bucle principal con manejo de errores

---

### 3_Codigo_Limpio.py - Arquitectura Limpia

**Nivel:** Intermedio-Avanzado

**Concepto central:** Separación de responsabilidades y uso de tipos enumerados para mejorar la legibilidad y mantenibilidad del código.

**Características principales:**
- Uso de `IntEnum` para definir las acciones del juego
- Separación clara de responsabilidades mediante funciones especializadas
- Entrada mediante índices numéricos en lugar de texto
- Generación dinámica de opciones desde el enum
- Manejo de excepciones con información de rango válido

**Conceptos de programación cubiertos:**
- Enumeraciones (Enum e IntEnum)
- Programación orientada a objetos (conceptos básicos)
- Separación de responsabilidades
- Arquitectura de código escalable
- Tipos seguros y validación

**Funciones principales:**
- `obtener_accion_usuario()`: Obtiene y valida la entrada del usuario
- `obtener_accion_computadora()`: Genera una acción aleatoria para la máquina
- `evaluar_juego()`: Determina el ganador
- `jugar_otra_ronda()`: Pregunta al usuario si desea continuar

---

### 4_IA_Basica.py - Inteligencia Artificial Simple

**Nivel:** Avanzado

**Concepto central:** Implementación de una estrategia de IA simple que aprende del comportamiento del usuario basándose en el resultado anterior.

**Características principales:**
- Enums para acciones y resultados del juego
- Mantenimiento de historial de acciones y resultados
- Estrategia de IA adaptable según el resultado previo
- Análisis del último movimiento del usuario
- Diccionario para mapear qué acción vence a otra

**Estrategia de IA implementada:**
1. Primera ronda: La computadora elige aleatoriamente
2. Si el usuario ganó: La computadora elige la acción que habría ganado esa ronda
3. Si el usuario perdió: La computadora cambia de estrategia (rotación cíclica de acciones)
4. Si fue empate: La computadora elige aleatoriamente

**Conceptos de programación cubiertos:**
- Historial y estado del programa
- Análisis de datos históricos
- Lógica condicional avanzada
- Patrones de decisión adaptativos
- Uso de diccionarios para mapeo de relaciones

**Funciones principales:**
- `obtener_accion_computadora()`: Elige basándose en el historial
- `obtener_accion_ganadora()`: Devuelve la acción que vence a otra
- `obtener_accion_aleatoria_computadora()`: Genera una acción aleatoria
- Gestión de historial en `main()`

---

### 5_Mas_IA.py - Inteligencia Artificial Avanzada

**Nivel:** Avanzado

**Concepto central:** Análisis estadístico de patrones recientes para predecir el comportamiento del usuario.

**Características principales:**
- Análisis estadístico de los últimos N movimientos del usuario
- Detección de la acción más frecuente en los movimientos recientes
- Estrategia basada en la predicción de patrones
- Uso de la función `mode()` del módulo `statistics`
- Constante configurable para el número de movimientos analizados

**Estrategia de IA avanzada:**
1. Recopila los últimos 5 movimientos del usuario
2. Calcula la acción más frecuente en esos movimientos usando `mode()`
3. Elige la acción que vence a esa opción más frecuente
4. Adapta su estrategia continuamente a medida que se recopilan más datos

**Conceptos de programación cubiertos:**
- Análisis estadístico (`statistics.mode()`)
- Detección de patrones en datos históricos
- Ventanas deslizantes de datos
- Lógica predictiva
- Optimización de estrategias basada en datos

**Funciones principales:**
- `obtener_accion_computadora()`: Elige basándose en análisis de patrones
- `obtener_accion_ganadora()`: Devuelve la acción que vence a otra
- `obtener_accion_aleatoria_computadora()`: Genera una acción aleatoria

---

## Ejecución de los Programas

### Método recomendado: Ejecutar con uv run

Este es el método más simple y no requiere activar explícitamente el entorno virtual. El comando `uv run` ejecuta automáticamente el script en el contexto del entorno virtual:

```bash
uv run 1_Basico.py
uv run 2_Control_Errores.py
uv run 3_Codigo_Limpio.py
uv run 4_IA_Basica.py
uv run 5_Mas_IA.py
```

### Método alternativo: Ejecutar con Python directamente

Si ha activado manualmente el entorno virtual, puede ejecutar los scripts directamente con `python`:

```bash
python 1_Basico.py
python 2_Control_Errores.py
python 3_Codigo_Limpio.py
python 4_IA_Basica.py
python 5_Mas_IA.py
```

### Controles de Juego

**Versiones 1 y 2 (entrada de texto):**
- Escribir: `piedra`, `papel`, `tijeras`
- Escribir: `salir` para terminar el programa

**Versiones 3, 4 y 5 (entrada numérica):**
- Escribir: `0` para Piedra
- Escribir: `1` para Papel
- Escribir: `2` para Tijeras
- Escribir: `s` o `n` cuando se pregunte por otra ronda

---

## Tabla de Progresión de Conceptos

| Concepto | Versión 1 | Versión 2 | Versión 3 | Versión 4 | Versión 5 |
|----------|-----------|-----------|-----------|-----------|-----------|
| Fundamentos básicos | Sí | Sí | Sí | Sí | Sí |
| Manejo de errores | Parcial | Sí | Sí | Sí | Sí |
| Enums/Tipos avanzados | No | No | Sí | Sí | Sí |
| Separación responsabilidades | Parcial | Parcial | Sí | Sí | Sí |
| IA adaptable | No | No | No | Sí | Sí |
| Análisis de patrones | No | No | No | No | Sí |
| Documentación completa | Sí | Sí | Sí | Sí | Sí |

---

## Características Transversales

Todas las versiones incluyen:

### Documentación
- Docstring en el módulo describiendo la implementación
- Docstrings en cada función explicando parámetros y valores devueltos
- Comentarios en líneas complejas para clarificar la lógica

### Validación y Robustez
- Validación de entrada del usuario
- Manejo de excepciones y errores
- Mensajes de error descriptivos que orientan al usuario

### Usabilidad
- Mensajes de bienvenida al iniciar el programa
- Salida elegante del programa con despedida
- Solicitud clara de acciones del usuario
- Formatos consistentes en toda la aplicación

### Calidad de Código
- Nombres de variables descriptivos y auto-documentables
- Constantes claramente definidas
- Lógica legible y bien estructurada
- Adherencia a convenciones de Python (PEP 8)

---

## Conceptos de Programación por Nivel

### Nivel Básico (Versión 1)
- Variables, constantes y tipos de datos básicos
- Funciones y definición de parámetros
- Estructura de control: if-elif-else
- Bucles: while
- Entrada/salida con input() y print()
- Importación de módulos (random)

### Nivel Intermedio (Versiones 2-3)
- Excepciones personalizadas y manejo con try-except
- Enumeraciones (Enum e IntEnum)
- Introducción a programación orientada a objetos
- Separación clara de responsabilidades
- Validación robusta de entrada
- Listas y comprensiones de listas

### Nivel Avanzado (Versiones 4-5)
- Gestión de estado e historial
- Patrones de decisión adaptativos
- Análisis de datos históricos
- Análisis estadístico (función mode)
- Lógica condicional compleja
- Predicción basada en patrones

---

## Sugerencias para Actividades Docentes

### Análisis de Código
- Comparar la complejidad progresiva entre versiones
- Identificar diferencias en la estructura y organización
- Analizar cómo mejora la mantenibilidad del código

### Actividades de Modificación
- Añadir estadísticas de victorias/derrotas
- Implementar un sistema de puntuación
- Extender el juego con opciones adicionales (lagarto, Spock)
- Modificar la estrategia de IA en las versiones 4 y 5

### Ejercicios de Extensión
- Crear una interfaz gráfica usando tkinter
- Guardar resultados en un archivo
- Implementar multijugador local
- Crear un sistema de dificultad progresiva
- Generar reportes estadísticos

---

## Notas Técnicas

- El código utiliza características estándar de Python sin dependencias externas
- La función `mode()` en la versión 5 requiere el módulo `statistics` (incluido en la librería estándar desde Python 3.4)
- El proyecto es totalmente compatible con sistemas Windows, macOS y Linux
- Cada versión es independiente y puede ejecutarse sin necesidad de las otras

---

## Deactivar el Entorno Virtual

Si ha activado manualmente el entorno virtual usando `source .venv/bin/activate` (macOS/Linux) o `.venv\Scripts\Activate.ps1` (Windows), puede desactivarlo cuando termine:

```bash
deactivate
```

Nota: Si usa `uv run` para ejecutar los scripts, no es necesario desactivar el entorno virtual ya que se gestiona automáticamente.

---

## Información de Contacto y Recursos

Para más información sobre los temas cubiertos:
- Documentación oficial de Python: https://docs.python.org/
- PEP 8 - Guía de estilo: https://www.python.org/dev/peps/pep-0008/
- Documentación de uv: https://docs.astral.sh/uv/
- Teoría de IA y Machine Learning: https://www.deeplearningbook.org/

---

**Versión del documento:** 1.0
**Última actualización:** 3 de noviembre de 2025
**Destinatarios:** Estudiantes del Curso de Especialización en Big Data e Inteligencia Artificial
**Material educativo:** Unidad 1 - Fundamentos de Programación e Introducción a IA
