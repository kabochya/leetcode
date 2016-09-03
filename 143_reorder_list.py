# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            one = two = head
            while two.next and two.next.next: #split
                two = two.next.next
                one = one.next
            two = one.next #move to 2nd list
            x = one.next = None
            one = two
            while one.next: # reverse
                x = one.next
                one.next = x.next
                x.next = two
                two = x
            while two: # weave
                x = head.next
                head.next = two
                head = x
                x = two.next
                two.next = head
                two = x
