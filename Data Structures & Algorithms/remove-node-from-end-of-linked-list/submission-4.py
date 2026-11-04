# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        skip=head
        count=n
        for i in range(n):
                skip=skip.next
        curr=head
        while(skip!=None):
            prev=curr
            curr=curr.next
            skip=skip.next
        if(prev==None):
            head=curr.next
        else:
            prev.next=curr.next

            
        return head
        