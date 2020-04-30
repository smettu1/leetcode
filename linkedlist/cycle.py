#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        hptr = fptr = head
        while hptr and fptr:
            hptr = hptr.next
            fptr = fptr.next
            if fptr:
                fptr = fptr.next
            else:
                return False
            if hptr == fptr:
                return True
        return False
        
