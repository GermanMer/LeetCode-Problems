#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

#You may not alter the values in the list's nodes, only nodes themselves may be changed.

#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]

#Example 2:
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]

#Constraints:
#The number of nodes in the list is n.
#1 <= k <= n <= 5000
#0 <= Node.val <= 1000

class ListNode:
    # Clase que representa un nodo en una lista enlazada
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Función auxiliar para contar los nodos restantes a partir de un nodo dado.
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        # Función auxiliar para invertir k nodos a partir de un nodo dado.
        def reverse_k_nodes(head, k):
            prev, curr = None, head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, head

        # Nodo ficticio para facilitar la manipulación de la lista
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Marcar el inicio del grupo actual
            group_start = group_prev.next

            # Contar los nodos restantes a partir del nodo de inicio del grupo actual
            count = count_nodes(group_start)
            # Si los nodos restantes son menos de k, no necesitamos invertirlos
            if count < k:
                break

            # Avanzar puntero al nodo que sigue al final del grupo
            group_end = group_start
            for _ in range(k):
                group_end = group_end.next

            # Invertir k nodos a partir del nodo de inicio del grupo actual
            new_start, new_end = reverse_k_nodes(group_start, k)
            # Conectar el nodo previo al inicio del nuevo grupo invertido
            group_prev.next = new_start
            # Conectar el final del nuevo grupo invertido al siguiente grupo
            new_end.next = group_end

            # Mover el puntero del nodo previo al final del nuevo grupo invertido
            group_prev = new_end

        # Devolver el primer nodo de la lista modificada (omitimos el nodo ficticio)
        return dummy.next

# Función auxiliar para crear una lista enlazada a partir de una lista de Python
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
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

# Ejemplo 1
head = create_linked_list([1, 2, 3, 4, 5])
k = 2
reversed_list = Solution().reverseKGroup(head, k)
print(linked_list_to_list(reversed_list))  # Output: [2, 1, 4, 3, 5]

# Ejemplo 2
head = create_linked_list([1, 2, 3, 4, 5])
k = 3
reversed_list = Solution().reverseKGroup(head, k)
print(linked_list_to_list(reversed_list))  # Output: [3, 2, 1, 4, 5]
