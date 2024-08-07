# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:  # loop run as long as curr not equal to none
            while curr.next and curr.val == curr.next.val: # both cond one curr.next exist and prev and next value are equal
                curr.next = curr.next.next #if equal then curr move next to next left the same one node 
            curr = curr.next #otherwise curr move to the next node if both are not equal
        return head # return list from the start 
