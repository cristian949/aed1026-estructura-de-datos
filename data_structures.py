"""
Implementación de estructuras de datos básicas: Pila y Cola.
La pila funciona con el principio LIFO y la cola con el principio FIFO.
"""

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, valor):
        self.elementos.append(valor)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, valor):
        self.elementos.append(valor)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

if __name__ == '__main__':
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    print("Elemento desapilado:", pila.desapilar())

    cola = Cola()
    cola.encolar('a')
    cola.encolar('b')
    print("Elemento desencolado:", cola.desencolar())
