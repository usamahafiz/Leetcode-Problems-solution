# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy # tail means current pointer on the dummy node
        while list1 and list2: # run as long as both lists not empty
            if list1.val < list2.val:
                tail.next = list1 #firstly place node of list1
                list1 = list1.next #node of list1 also move one place ahead
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #tail also move next node to merge both sorted lists and at last None appear indicate both lists ended
        if list1: #run as long as list1 is not empty
            tail.next = list1 
        elif list2: #if list1  is empty then remaining number of list2 attaches the node 
            tail.next = list2
        return dummy.next

#time complexity O(n+m) bcz loop iterates each nodes of both lists 
#space complexity O(1)

        