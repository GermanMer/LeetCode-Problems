#You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

#Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

##Tienes un array de enteros llamado nums. Cada número en el array representa cuántos índices hacia adelante puedes saltar desde esa posición. Por ejemplo, si estás en la posición i y nums[i] es 3, puedes saltar hasta 3 posiciones hacia adelante, es decir, a i+1, i+2, o i+3.

#0 <= j <= nums[i] and
#i + j < n
#Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

#Example 1:
#Input: nums = [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    ##Desde nums[0] (que es 2), puedes saltar hasta nums[1] o nums[2].
    ##Si saltas a nums[1] (donde el valor es 3), puedes saltar hasta nums[2], nums[3] o nums[4].
    ##Saltando a nums[4], alcanzas el final. Entonces, el número mínimo de saltos es 2: primero saltas a nums[1], luego a nums[4].

#Example 2:
#Input: nums = [2,3,0,1,4]
#Output: 2

#Constraints:
#1 <= nums.length <= 104
#0 <= nums[i] <= 1000
#It's guaranteed that you can reach nums[n - 1].

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Cola para BFS (Breadth-First Search o Búsqueda en Anchura): almacena pares (índice, número de saltos)
        queue = [(0, 0)]  # Comienza desde el índice 0 con 0 saltos
        visited = set()  # Conjunto para marcar los índices visitados
        visited.add(0)

        while queue:
            # Extraer el primer elemento de la cola
            current_index, jumps = queue.pop(0)

            # Si hemos alcanzado el último índice, devolvemos el número de saltos
            if current_index == n - 1:
                return jumps

            # Saltos posibles desde el índice actual
            max_jump = nums[current_index]

            for next_index in range(current_index + 1, min(current_index + max_jump + 1, n)):
                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, jumps + 1))

        return -1  # En caso de que no se pueda alcanzar el último índice (esto no debería suceder según el enunciado)

#Example 1:
nums = [2,3,1,1,4]
#Output: 2
print(Solution().jump(nums))

#Example 2:
nums = [2,3,0,1,4]
#Output: 2
print(Solution().jump(nums))

#BFS, o Búsqueda en Anchura (en inglés Breadth-First Search), es un algoritmo utilizado para explorar nodos y aristas en un grafo o en estructuras similares, como un árbol. Es útil para encontrar la ruta más corta en términos de número de aristas desde un nodo inicial hasta otros nodos en un grafo no ponderado.

#Cómo Funciona BFS
    #Inicialización:
        #Comienza en el nodo inicial (o raíz) y lo marca como visitado.
        #Usa una estructura de datos llamada cola para mantener un registro de los nodos que se deben explorar.
    #Exploración:
        #Extrae el nodo al frente de la cola (el nodo más antiguo en la cola).
        #Explora todos sus nodos vecinos (o hijos en el caso de árboles).
        #Para cada vecino no visitado, lo marca como visitado y lo añade a la cola.
    #Repetición:
        #Repite el proceso hasta que la cola esté vacía o se haya encontrado el objetivo.

#Características de BFS
    #Explora Nivel por Nivel: BFS explora todos los nodos en el nivel actual antes de pasar al siguiente nivel. Esto asegura que encuentra la solución más cercana (más corta en términos de número de aristas) primero.
    #Uso de Cola: La cola es fundamental para mantener el orden en el que se exploran los nodos. La naturaleza FIFO (First In, First Out) de la cola asegura que los nodos se exploran en el orden en que se añaden.

#Aplicaciones Comunes de BFS
    #Encontrar la Ruta Más Corta: En un grafo no ponderado, BFS puede encontrar la ruta más corta desde un nodo inicial hasta un nodo objetivo en términos de número de aristas.
    #Construcción de Árboles de Expansión: BFS se usa para construir un árbol de expansión mínimo en grafos no ponderados.
    #Resolución de Laberintos: BFS es útil para encontrar el camino más corto en laberintos.
    #Problemas de Niveles en Grafos: Para problemas que requieren explorar niveles o capas de nodos, como en redes o sistemas de comunicación.

#Contexto del Problema
#Dado un array nums en el que cada elemento nums[i] indica el máximo número de índices a los que puedes saltar hacia adelante desde el índice i, debes encontrar el número mínimo de saltos necesarios para llegar desde el primer índice (nums[0]) al último índice (nums[n - 1]).
#Aplicación de BFS al Problema de Saltos
    #Modelo del Problema como un Grafo:
        #Piensa en cada índice del array como un nodo en un grafo.
        #Un salto desde el índice i a i + j (donde 0 <= j <= nums[i] y i + j < n) puede considerarse como una arista o conexión entre los nodos i e i + j.
    #Objetivo:
        #Encuentra el camino más corto (en términos de número de saltos) desde el nodo inicial (nums[0]) al nodo final (nums[n - 1]).
#Cómo BFS Resuelve el Problema
    #Inicialización:
        #Inicio: Comienza en el índice 0 con 0 saltos.
        #Cola: Usa una cola para explorar los índices. La cola almacenará tuplas que consisten en un índice y el número de saltos realizados hasta llegar a ese índice.
        #Conjunto de Visitados: Usa un conjunto para llevar un registro de los índices que ya has visitado para evitar ciclos y exploraciones redundantes.
    #Proceso:
        #Exploración Nivel por Nivel:
            #Extrae el índice más antiguo de la cola (es decir, el nodo que se agregó primero y que se encuentra al frente de la cola).
            #Desde el índice actual, calcula todos los índices a los que puedes saltar (es decir, los nodos vecinos). Estos índices son accesibles según el valor en nums[i].
            #Añade estos nuevos índices a la cola si no han sido visitados previamente.
            #Marca como Visitado: Asegúrate de marcar cada nuevo índice como visitado cuando lo añades a la cola para evitar explorar el mismo índice varias veces.
    #Detección del Objetivo:
        #Llegar al Último Índice: Si en cualquier punto extraes el último índice (n - 1) de la cola, significa que has encontrado el camino más corto en términos de número de saltos, y puedes devolver el número de saltos realizados.
#Ejemplo Paso a Paso
#Supongamos que nums = [2, 3, 1, 1, 4]:
    #Inicialización:
        #Cola: [(0, 0)] (índice 0 con 0 saltos)
        #Visitados: {0}
    #Primera Iteración:
        #Extrae (0, 0) de la cola.
        #Desde 0, puedes saltar a los índices 1 y 2.
        #Añade (1, 1) y (2, 1) a la cola.
        #Cola: [(1, 1), (2, 1)]
        #Visitados: {0, 1, 2}
    #Segunda Iteración:
        #Extrae (1, 1) de la cola.
        #Desde 1, puedes saltar a los índices 2, 3, y 4.
        #Añade (3, 2) y (4, 2) a la cola. (Nota: 2 ya está visitado)
        #Cola: [(2, 1), (3, 2), (4, 2)]
        #Visitados: {0, 1, 2, 3, 4}
    #Tercera Iteración:
        #Extrae (2, 1) de la cola.
        #Desde 2, puedes saltar a los índices 3 y 4. (Ambos ya están visitados)
    #Cuarta Iteración:
        #Extrae (3, 2) de la cola.
        #Desde 3, puedes saltar a 4, que es el último índice. (Este es el objetivo)
    #Resultado:
        #El número mínimo de saltos es 2.
