# Hoja-de-trabajo-3-algoritmos-y-estructura-de-los-datos
Hoja de trabajo
Este es un programa que simula la ejecución de procesos en un sistema operativo utilizando el paradigma de simulación de eventos discretos. Se utiliza la biblioteca SimPy para modelar y simular los recursos del sistema, como la memoria RAM y la unidad central de procesamiento (CPU)

Autor
Hugo Barillas
Descripción del Código
El código simula la ejecución de múltiples procesos en un sistema operativo, donde cada proceso realiza una serie de instrucciones que requieren acceso a la memoria RAM y a la CPU

Funcionalidades Principales
Programa: Define la clase Programa que representa un proceso en el sistema. Cada proceso solicita memoria RAM y utiliza la CPU para ejecutar un número aleatorio de instrucciones
Simulación: La función simular crea y ejecuta varios procesos en un entorno de simulación
Gráficas: La función generar_graficas realiza simulaciones con diferentes cantidades de procesos y grafica el tiempo promedio en el sistema en función del número de procesos
Bibliotecas Utilizadas
simpy: Para modelar y simular sistemas basados en eventos discretos
random: Para la generación de números aleatorios
numpy: Para operaciones matemáticas
matplotlib.pyplot: Para la generación de gráficas
Uso del Código
Para ejecutar el código y generar las gráficas, simplemente ejecutar el código. Las gráficas resultantes mostrarán el tiempo promedio en el sistema en función del número de procesos simulados

Notas
El código utiliza una semilla aleatoria (RANDOM_SEED) para garantizar la reproducibilidad de los resultados
Cada gráfica se genera realizando 10 simulaciones para obtener un promedio más confiable del tiempo promedio en el sistema, ya que no me dejó hacer la gráfica por proceso individual, que no lograba que se mostrara bien la gráfica


Cómo mejorar el rendimiento:

La asignación de recursos: Asignar más recursos al momento de correr los procesos.

Optimizar los tiempos de los procesos: El algoritmo de planificación determina cómo se asigna el tiempo de la CPU entre los procesos en ejecución. 

Aumento de la capacidad de la memoria RAM: Incrementar la cantidad de memoria RAM disponible para los procesos.