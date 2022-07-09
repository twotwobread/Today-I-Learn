# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        tmp = head
        while True:
            if tmp.next == None:
                new = tmp
                break
            tmp = tmp.next
        while True:
            temp = head
            if temp.next == None:
                break
            while True:
                if temp.next.next == None:
                    temp.next.next = temp
                    temp.next = None
                    break
                temp = temp.next
        return new
                
                
                    
