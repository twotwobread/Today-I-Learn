# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        if list1 != None and list2 !=None:
            if list1.val < list2.val:
                result.val = list1.val
                list1 = list1.next
            else:
                result.val = list2.val
                list2 = list2.next
        elif list1 != None:
            return list1
        elif list2 != None:
            return list2
        else:
            return None
        realResult = result
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = ListNode(list1.val, None)
                result.next = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val, None)
                result.next = temp
                list2 = list2.next
            result = result.next
        if list1 != None:
            result.next = list1
        if list2 != None:
            result.next = list2
        return realResult
                    
                    
                
                
        
