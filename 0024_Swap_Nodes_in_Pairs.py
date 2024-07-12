#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#Example 1:
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]

#Example 2:
#Input: head = []
#Output: []

#Example 3:
#Input: head = [1]
#Output: [1]

#Constraints:
#The number of nodes in the list is in the range [0, 100].
#0 <= Node.val <= 100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            # Mientras haya al menos dos nodos para intercambiar (es decir, current.next y current.next.next no son None).
            first = current.next
            second = current.next.next

            # Intercambiar los nodos
            first.next = second.next
            second.next = first
            current.next = second

            # Mover el puntero al siguiente par
            current = first

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

# Función auxiliar para convertir una lista enlazada en una lista.
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

#Example 1:
head = create_linked_list([1,2,3,4])
swap_list = Solution().swapPairs(head)
print(linked_list_to_list(swap_list))  # Output: [2,1,4,3]

#Example 2:
head = create_linked_list([])
swap_list = Solution().swapPairs(head)
print(linked_list_to_list(swap_list))  # Output: []

#Example 3:
head = create_linked_list([1])
swap_list = Solution().swapPairs(head)
print(linked_list_to_list(swap_list))  # Output: [1]
