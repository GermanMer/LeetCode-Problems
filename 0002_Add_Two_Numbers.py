#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example 1:
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

#Example 2:
#Input: l1 = [0], l2 = [0]
#Output: [0]

#Example 3:
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize the dummy node which helps to simplify the code when adding new nodes
        dummy = ListNode()
        # This will be the current node in the result linked list
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get the current values, if the node is not null, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of values and the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            # Create a new node and move the pointer
            current.next = ListNode(new_val)
            current = current.next

            # Move to the next nodes in the lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # The dummy.next is the head of the new linked list
        return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

#Example 1:
l1 = build_linked_list([2,4,3])
l2 = build_linked_list([5,6,4])
print_linked_list(Solution().addTwoNumbers(l1, l2)) #Output: 7 0 8

#Example 2:
l1 = build_linked_list([0])
l2 = build_linked_list([0])
print_linked_list(Solution().addTwoNumbers(l1, l2)) #Output: 0

#Example 3:
l1 = build_linked_list([9,9,9,9,9,9,9])
l2 = build_linked_list([9,9,9,9])
print_linked_list(Solution().addTwoNumbers(l1, l2)) #Output: 8 9 9 9 0 0 0 1
