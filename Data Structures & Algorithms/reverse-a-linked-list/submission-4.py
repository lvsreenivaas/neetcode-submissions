# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next
            
        # 2. Reverse the regular list
        values.reverse()
        
        # 3. Put the reversed values back into the nodes
        current = head
        for val in values:
            current.val = val
            current = current.next
            
        return head