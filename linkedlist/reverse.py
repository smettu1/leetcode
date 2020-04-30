#https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        hd_ptr = head
        #create a new node
        if not head:
            return 
        temp = ListNode(hd_ptr.val)
        temp.next = hd_ptr.next
        while hd_ptr:
            #move the ptr
            temp = hd_ptr
            hd_ptr = hd_ptr.next
            if hd_ptr:
                print("hd ",hd_ptr.val)
                print(" temp",temp.val)
                temp.next = prev
                prev = temp
                print("prev ",prev.val)
            else:
                temp.next = prev
                return temp
            
        
