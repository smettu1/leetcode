#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        temp = ListNode(l1.val)
        head = None
        while (l1 and l2):
            if l1.val <= l2.val:
                print("l1 is hight moving it")
                if temp.next:
                    temp.next = l1
                temp = l1
                l1= l1.next
                print("temp: ",temp.val,"l1:",l1.val if l1 else -1)
                temp.next = l2
                if l1 is None:
                    temp.next = l2
                if head is None:
                    head = temp
            else:
                print("l2 is hight moving it")
                if temp.next:
                    temp.next = l2
                temp = l2
                l2 = l2.next
                print("temp: ",temp.val,"l2:",l2.val if l2 else -1)
                if l2 is None:
                    temp.next = l1
                if head is None:
                    head = temp
        return head
