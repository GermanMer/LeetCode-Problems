#Given the head of a linked list, remove the nth node from the end of the list and return its head.

#Example 1:
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]

#Example 2:
#Input: head = [1], n = 1
#Output: []

#Example 3:
#Input: head = [1,2], n = 1
#Output: [1]

#Constraints:
#The number of nodes in the list is sz.
#1 <= sz <= 30
#0 <= Node.val <= 100
#1 <= n <= sz

# Definición de la clase para la lista enlazada simple.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Creamos un nodo ficticio que apunta al principio de la lista y dos punteros (first y second).
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Movemos el puntero 'first' n+1 posiciones hacia adelante para mantener una distancia de n nodos con 'second'.
        for _ in range(n + 1):
            first = first.next

        # Movemos ambos punteros hasta que 'first' alcance el final de la lista.
        while first:
            first = first.next
            second = second.next

        # Eliminamos el nodo n-ésimo desde el final ajustando el puntero 'next' del nodo anterior.
        second.next = second.next.next

        # Retornamos la cabeza de la nueva lista.
        return dummy.next

# Función auxiliar para crear una lista enlazada a partir de una lista.
def create_linked_list(lst):
    # Creamos un nodo ficticio que facilita la construcción de la lista.
    dummy = ListNode(0)
    current = dummy
    # Iteramos sobre cada valor en la lista y creamos un nuevo nodo en la lista enlazada.
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    # Retornamos la cabeza de la lista enlazada, omitiendo el nodo ficticio inicial.
    return dummy.next

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
head = create_linked_list([1,2,3,4,5])
n = 2
result = Solution().removeNthFromEnd(head, n)
# Convertimos el resultado de la lista enlazada a una lista y lo imprimimos.
print(linked_list_to_list(result))  # Output: [1, 2, 3, 5]

# Ejemplo 2
head = create_linked_list([1])
n = 1
result = Solution().removeNthFromEnd(head, n)
# Convertimos el resultado de la lista enlazada a una lista y lo imprimimos.
print(linked_list_to_list(result))  # Output: []

# Ejemplo 3
head = create_linked_list([1,2])
n = 1
result = Solution().removeNthFromEnd(head, n)
# Convertimos el resultado de la lista enlazada a una lista y lo imprimimos.
print(linked_list_to_list(result))  # Output: [1]
