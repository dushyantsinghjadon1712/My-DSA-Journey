"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium

Approach: Simulate digit-by-digit addition (like adding on paper).
Since digits are stored in reverse order, the least significant
digit comes first, which matches how addition naturally works
right to left. Use a dummy head node to simplify building the
result list, and track a carry across each step.

Time: O(max(m, n))
Space: O(max(m, n)) for the output list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next