# Importamos las bibliotecas necesarias
import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

# Semilla para reproducibilidad
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Función para obtener el tiempo inicial
def tiempo_inicial(env):
    return env.now

# Función para obtener el tiempo final
def tiempo_final(env, tiempo_inicial):
    return env.now - tiempo_inicial

# Definición de la clase Programa que simula un proceso
class Programa:
    def __init__(self, name, env, ram, cpu):
        self.name = name
        self.memoria = random.randint(1, 10)
        self.num_instrucciones = random.randint(1, 10)
        self.env = env
        self.ram = ram
        self.cpu = cpu
        self.tiempo_inicio = None
        self.tiempo_fin = None

    #Método para solicitar memoria RAM
    def pedir_memoria(self):
        print(f"{self.name}: Solicitando {self.memoria} de memoria RAM")
        yield self.ram.get(self.memoria)
        print(f"{self.name}: Obtenida memoria RAM")

    # Método para utilizar el CPU
    def usar_cpu(self):
        with self.cpu.request() as req:
            print(f"{self.name}: Esperando CPU")
            yield req
            print(f"{self.name}: Obtenido CPU")
            while self.num_instrucciones > 0:
                instrucciones_ejecutadas = min(3, self.num_instrucciones)
                yield self.env.timeout(1)  # Simula una instrucción ejecutada en 1 unidad de tiempo
                self.num_instrucciones -= instrucciones_ejecutadas
                print(f"{self.name}: Ejecutadas {instrucciones_ejecutadas} instrucciones, restantes: {self.num_instrucciones}")
                if self.num_instrucciones == 0:
                    break

    # Método principal para ejecutar el programa
    def run(self):
        self.tiempo_inicio = tiempo_inicial(self.env)  # Almacenar el tiempo inicial
        yield self.env.process(self.pedir_memoria())  # Procesar la solicitud de memoria RAM
        yield self.env.process(self.usar_cpu())       # Procesar el uso del CPU
        self.tiempo_fin = tiempo_final(self.env, self.tiempo_inicio)  # Almacenar el tiempo final
        print(f"{self.name}: Proceso completado")
        self.ram.put(self.memoria)  # Liberar la memoria RAM utilizada por el proceso

#Función para simular la ejecución de procesos
def simular(env, num_procesos):
    ram = simpy.Container(env, init=100, capacity=100)
    cpu = simpy.Resource(env, capacity=1)
    procesos = []
    # Crear y ejecutar los procesos
    for i in range(num_procesos):
        proceso = Programa(f"Proceso_{i}", env, ram, cpu)
        env.process(proceso.run())
        procesos.append(proceso)
    env.run()  # Ejecutar la simulación

    # Calcular el tiempo promedio y la desviación estándar de los tiempos de los procesos
    tiempos_en_sistema = [proceso.tiempo_fin for proceso in procesos]
    tiempo_promedio = np.mean(tiempos_en_sistema)
    desviacion_estandar = np.std(tiempos_en_sistema)
    return tiempo_promedio, desviacion_estandar

# Función para generar las gráficas
def generar_graficas():
    num_procesos_por_grafica = [20, 50, 100, 150, 200]
    #Sobre el número de procesos por gráfica
    for num_procesos in num_procesos_por_grafica:
        tiempos_promedio = []
        #Repetir la simulación 10 veces para obtener un promedio más confiable
        for _ in range(10):
            env = simpy.Environment()
            tiempo_promedio, _ = simular(env, num_procesos)
            tiempos_promedio.append(tiempo_promedio)
        # Graficar los tiempos promedio para el número de procesos actual
        plt.plot(range(1, 11), tiempos_promedio, label=f'{num_procesos} procesos')
    plt.xlabel('Iteración')
    plt.ylabel('Tiempo promedio en el sistema')
    plt.title('Tiempo promedio en el sistema en función del número de procesos')
    plt.legend()
    plt.show()

#Función principal que genera las gráficas
if __name__ == '__main__':
    generar_graficas()