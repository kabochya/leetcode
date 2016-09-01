# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c,ret,z = 0,l1,ListNode(0)
        main,aux = l1,l2
        z.next = z
        while True:
            val = main.val+aux.val+c
            main.val, c = val%10, val/10
            if not main.next:
                if not aux.next or aux==z:
                    break
                aux = aux.next
                main.next = aux
                aux, main = z, aux
            else:
                main = main.next
                aux = aux.next if aux.next else z
        if c:
            main.next=ListNode(1)
        return ret
