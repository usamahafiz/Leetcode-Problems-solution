# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            next_node = current.next # variable current move next and it's value store in node_next variable 
            current.next = prev # step to reverse current pointer's node
            prev = current # moved prev to current node but not at node_next node  bcz at last prev move to the new head
            current = next_node # current move one node ahead
            head = prev
        return head

        