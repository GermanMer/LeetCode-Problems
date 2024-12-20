# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# Constraints:
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

from typing import Optional

# Definición del nodo de la lista enlazada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Crear dos listas enlazadas separadas usando nodos "dummy"
        less_head = ListNode(0)  # Lista para nodos con valor < x
        greater_head = ListNode(0)  # Lista para nodos con valor >= x

        less = less_head  # Puntero para la lista 'less'
        greater = greater_head  # Puntero para la lista 'greater'
        current = head  # Puntero para recorrer la lista original

        # Recorre la lista original
        while current:
            if current.val < x:
                # Añade el nodo a la lista 'less'
                less.next = current
                less = less.next
            else:
                # Añade el nodo a la lista 'greater'
                greater.next = current
                greater = greater.next
            current = current.next  # Avanza al siguiente nodo

        # Enlaza la lista 'less' con la lista 'greater'
        less.next = greater_head.next
        greater.next = None  # Evita ciclos cerrando la lista 'greater'

        # Retorna la cabeza de la nueva lista
        return less_head.next

# Función para crear una lista enlazada a partir de una lista de Python
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
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
head = [1,4,3,2,5,2]
x = 3
linked_list = create_linked_list(head)
print(linked_list_to_list(Solution().partition(linked_list, x)))
# Output: [1,2,2,4,3,5]

# Example 2:
head = [2,1]
x = 2
linked_list = create_linked_list(head)
print(linked_list_to_list(Solution().partition(linked_list, x)))
# Output: [1,2]
