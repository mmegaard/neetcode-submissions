# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #handle empty lists, if one is empty the other is the merged list
        if not list1:
            return list2
        if not list2:
            return list1
        #pick the head we will track by choosing the lowest starting val
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        #point another pointer at the head so we can always know what the end of our merged list is
        tail = head
        while list1 and list2:
            #point the tail.next to the lower value
            #advance the list that contained the value we just pointed to
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            #advance the tail to the node we just added, either list1 or list2
            tail = tail.next
        #point the tail to the remaining value, one will always be None after while loop
        tail.next = list1 if list1 else list2
        #return head which is still pointing at the beginning of tail
        return head