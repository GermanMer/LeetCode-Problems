# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Paso 1: Calcular la longitud de la lista
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Paso 2: Reducir k si es mayor que la longitud
        k = k % length
        if k == 0:
            return head

        # Paso 3: Encontrar el nuevo final de la lista
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next  # El nuevo head será el siguiente del nuevo tail
        new_tail.next = None  # Cortamos la lista en el nuevo tail
        current.next = head  # Hacemos que el último nodo apunte al head original

        return new_head

def print_list(head: ListNode):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example 1:
head = [1, 2, 3, 4, 5]
k = 2
linked_list = create_list(head)
print_list(Solution().rotateRight(linked_list, k))
# Output: [4,5,1,2,3]

# Example 2:
head = [0, 1, 2]
k = 4
linked_list = create_list(head)
print_list(Solution().rotateRight(linked_list, k))
# Output: [2,0,1]
