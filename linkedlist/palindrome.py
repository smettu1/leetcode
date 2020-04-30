#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = []
        hptr = head
        if head ==None:
            return True
        while hptr:
            p.append(hptr.val)
            hptr = hptr.next
        hptr = head
        print("list is ",p)
        while hptr:
            if hptr.val != p.pop():
                return False
            hptr = hptr.next
        return True
        
