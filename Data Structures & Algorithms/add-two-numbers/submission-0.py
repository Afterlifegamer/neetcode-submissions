# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(None)
        curr=dummy
        while(l1 and l2):
            if(carry==1):
                sums=l1.val+l2.val+carry
                carry=0
            else:
                sums=l1.val+l2.val
            if(sums>9):
                sums=sums%10
                carry=1
            curr.next=ListNode(sums)
            curr=curr.next
            l1=l1.next
            l2=l2.next
            
            
            
            
        while(l1):
            if(carry==1):
                sums=l1.val+carry
                carry=0
            else:
                sums=l1.val
            if(sums>9):
                sums=sums%10
                carry=1
            curr.next=ListNode(sums)
            curr=curr.next
            l1=l1.next
        while(l2):
            if(carry==1):
                sums=l2.val+carry
                carry=0
            else:
                sums=l2.val
            if(sums>9):
                sums=sums%10
                carry=1
            curr.next=ListNode(sums)
            curr=curr.next
            l2=l2.next
        if(carry==1):
            curr.next=ListNode(1)
        return dummy.next


        