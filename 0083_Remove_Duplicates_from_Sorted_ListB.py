# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

from typing import Optional

# Definición de la clase ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solución para eliminar duplicados de una lista enlazada ordenada
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # Inicia desde el nodo cabeza

        while current and current.next:  # Mientras haya nodos a verificar
            if current.val == current.next.val:
               # Si el actual y el siguiente tienen el mismo valor, salta el duplicado
                current.next = current.next.next
            else:
                # Si no son duplicados, avanza al siguiente nodo
                current = current.next

        return head  # Retorna la cabeza de la lista actualizada

# Función para crear una lista enlazada a partir de una lista de Python
def create_linked_list(arr):
    if not arr:  # Si la lista está vacía, devuelve None
        return None
    head = ListNode(arr[0])  # Crea el primer nodo
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)  # Crea el siguiente nodo y lo enlaza
        current = current.next
    return head

# Función para convertir una lista enlazada en una lista de Python
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1:
head = create_linked_list([1,1,2])
print(linked_list_to_list(Solution().deleteDuplicates(head)))
# Output: [1, 2]

# Example 2:
head = create_linked_list([1,1,2,3,3])
print(linked_list_to_list(Solution().deleteDuplicates(head)))
# Output: [1, 2, 3]
