#https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def ismirror(r1,r2):
            if not r1 and not r2:
                return True
            if r1 and not r2:
                return False
            if r2 and not r1:
                return False
            print("Checking ",r1.val,r2.val)
            if r1.val == r2.val and ismirror(r1.left,r2.right) and ismirror(r1.right,r2.left):
                return True
            return False
        return ismirror(root,root)
        
