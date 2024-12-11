# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Nodo ficticio que ayuda a simplificar la lógica de eliminación
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # 'prev' es el nodo antes de 'current'
        current = head  # 'current' es el nodo actual

        while current:
            # Si el siguiente nodo tiene el mismo valor que el actual, es un duplicado
            if current.next and current.val == current.next.val:
                # Avanza mientras haya nodos duplicados
                while current.next and current.val == current.next.val:
                    current = current.next
                # Salta todos los nodos duplicados
                prev.next = current.next
            else:
                # Si no es un duplicado, simplemente avanza
                prev = prev.next

            # Avanza al siguiente nodo
            current = current.next

        return dummy.next  # Retorna la cabeza de la lista sin duplicados

# Función para crear una lista enlazada a partir de una lista de Python
def create_linked_list(arr):
    head = ListNode(arr[0])  # Crea el primer nodo
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)  # Crea el siguiente nodo y lo enlaza
        current = current.next
    return head

# Función auxiliar para convertir una lista enlazada en una lista de Python
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1:
head = create_linked_list([1, 2, 3, 3, 4, 4, 5])
print(linked_list_to_list(Solution().deleteDuplicates(head)))
# Output: [1, 2, 5]

# Example 2:
head = create_linked_list([1, 1, 1, 2, 3])
print(linked_list_to_list(Solution().deleteDuplicates(head)))
# Output: [2, 3]
