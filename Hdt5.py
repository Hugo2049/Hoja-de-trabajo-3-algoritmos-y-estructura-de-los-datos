import sympy
import random

class Programa:

    def __init__(self, name, env, ram, procesador):
        self.name = name
        self.memoria = 10 # cambiar
        self.num_instruc = 5 # cambiar
        

    def pedir_memoria(self):
        print("Pidiendo memoria")
        # cambiar

    def usar_cpu(self):
        yield self.env.timeout(10)
        print("Pidiendo cpu.")

    def pedir_io(self):
        print("Pidiendo io.")

    def run(self):
        # logica de como cambiar de estados
        # Pedir memoria
        # with request etc
            # pedir cpu
        yield self.env.timeout(10)
            # ejecutar 3 instrucciones
            # ponga un timeout
            # pedir io/o no
            # esperar
            # fin

def simular(env, param):
    #cambiar
    print("Simulando....")
        
# Cambiar a procesos
        
env = sympy.Environment()
track = sympy.Resource(env, capacity=1)  # Define the race track as a shared resource
print("Llamada a simular")
env.process(simular(env, track))

env.run()