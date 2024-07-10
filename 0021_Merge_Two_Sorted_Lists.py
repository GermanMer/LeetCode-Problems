#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

#Example 1:
#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]

#Example 2:
#Input: list1 = [], list2 = []
#Output: []

#Example 3:
#Input: list1 = [], list2 = [0]
#Output: [0]

#Constraints:
#The number of nodes in both lists is in the range [0, 50].
#-100 <= Node.val <= 100
#Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    # Clase que representa un nodo en una lista enlazada
    def __init__(self, val=0, next=None):
        # Constructor de la clase, inicializa el valor y el siguiente nodo
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Función para fusionar dos listas enlazadas ordenadas

        # Crear un nodo ficticio (dummy) para facilitar la construcción de la lista fusionada
        dummy = ListNode()
        # Puntero actual que se moverá a lo largo de la nueva lista
        current = dummy

        # Mientras ambos list1 y list2 no estén vacíos
        while list1 and list2:
            # Comparar los valores de los nodos actuales de list1 y list2
            if list1.val < list2.val:
                # Si el valor del nodo en list1 es menor, enlazarlo a la nueva lista
                current.next = list1
                # Avanzar al siguiente nodo en list1
                list1 = list1.next
            else:
                # Si el valor del nodo en list2 es menor o igual, enlazarlo a la nueva lista
                current.next = list2
                # Avanzar al siguiente nodo en list2
                list2 = list2.next
            # Avanzar el puntero de la nueva lista
            current = current.next

        # Si quedan nodos en list1, enlazarlos a la nueva lista
        if list1:
            current.next = list1
        # Si quedan nodos en list2, enlazarlos a la nueva lista
        elif list2:
            current.next = list2

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
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = Solution().mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]

# Ejemplo 2
list1 = create_linked_list([])
list2 = create_linked_list([])
merged_list = Solution().mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: []

# Ejemplo 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged_list = Solution().mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [0]
