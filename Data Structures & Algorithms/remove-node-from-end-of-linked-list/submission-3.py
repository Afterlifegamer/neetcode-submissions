# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        current=head
        count=n
        next_node=current
        while(count!=0):
            next_node=next_node.next
            count=count-1
        
        while(current!=None):
            if(next_node==None):
                if(prev==None and current.next==None):
                    return None
                elif(prev==None):
                    head=current.next
                    break
                else:
                    prev.next=current.next
                
                    break
            prev=current
            current=current.next
            next_node=next_node.next
        return head
                
        