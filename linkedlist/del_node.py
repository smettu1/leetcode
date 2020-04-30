#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print (dir(self))
        while node:
            print(node.val)
            next_node = node.next
            if next_node:
                print('next node is present')
                node.val = next_node.val
                if next_node.next == None:
                    node.next = None 
                    break
                node = node.next
            else:
                print('at end ')
                node.next = None
                node.val = None
                node = None
                next_node = None

