#https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = (pow(2,32)-1)*-1
        max_val = pow(2,32)
        def is_validbst(root, min_val, max_val):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            left_ok = True
            right_ok = True
            if root.left:
                left_ok= is_validbst(root.left,min_val,root.val)
            if root.right:
                right_ok = is_validbst(root.right,root.val,max_val)
            if ( left_ok and right_ok):
                return True
            return False

        return is_validbst(root,min_val,max_val)
