# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        L = R = head

        while R and R.next:
            L = L.next
            R = R.next.next
            if L == R:
                return True
        return False