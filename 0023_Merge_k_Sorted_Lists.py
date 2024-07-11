#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6

#Example 2:
#Input: lists = []
#Output: []

#Example 3:
#Input: lists = [[]]
#Output: []

#Constraints:
#k == lists.length
#0 <= k <= 104
#0 <= lists[i].length <= 500
#-104 <= lists[i][j] <= 104
#lists[i] is sorted in ascending order.
#The sum of lists[i].length will not exceed 104.

import heapq
from typing import List, Optional

class ListNode:
    # Clase que representa un nodo en una lista enlazada
    def __init__(self, val=0, next=None):
        # Constructor de la clase, inicializa el valor y el siguiente nodo
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Función para fusionar k listas enlazadas ordenadas

        # Crear un nodo ficticio (dummy) para facilitar la construcción de la lista fusionada
        dummy = ListNode(0)
        # Puntero actual que se moverá a lo largo de la nueva lista
        current = dummy

        # Crear una lista (heap) para manejar la cola de prioridad
        heap = []

        # Insertar el primer nodo de cada lista en el heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        # Mientras haya elementos en el heap
        while heap:
            # Obtener el nodo con el menor valor
            val, i, node = heapq.heappop(heap)
            # Enlazar este nodo a la nueva lista
            current.next = node
            # Avanzar el puntero de la nueva lista
            current = current.next
            # Si hay un siguiente nodo en la lista actual, insertarlo en el heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Devolver el primer nodo de la nueva lista fusionada (omitimos el nodo ficticio)
        return dummy.next

def create_linked_list(arr):
    # Función auxiliar para crear una lista enlazada a partir de una lista de Python

    # Si la lista está vacía, devolver None
    if not arr:
        return None
    # Crear el primer nodo de la lista enlazada
    head = ListNode(arr[0])
    # Puntero actual para construir la lista
    current = head
    # Iterar sobre los valores restantes y crear nodos enlazados
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    # Devolver el nodo cabeza de la lista enlazada
    return head

# Función auxiliar para convertir una lista enlazada en una lista.
def linked_list_to_list(head):
    result = []
    current = head
    # Iteramos sobre cada nodo en la lista enlazada y agregamos su valor a una lista.
    while current:
        result.append(current.val)
        current = current.next
    # Retornamos la lista resultante.
    return result

# Ejemplo 1
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]
merged_list = Solution().mergeKLists(lists)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

# Ejemplo 2
lists = []
merged_list = Solution().mergeKLists(lists)
print(linked_list_to_list(merged_list))  # Output: []

# Ejemplo 3
lists = [create_linked_list([])]
merged_list = Solution().mergeKLists(lists)
print(linked_list_to_list(merged_list))  # Output: []
