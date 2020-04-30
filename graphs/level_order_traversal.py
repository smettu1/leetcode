#https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        resp = {}
        q = [] 
        if not root:
            return []
        #q.insert(0,val)
        #q.pop(0)
        tmp = root
        count = 1
        while tmp:
            print(tmp.val,count)
            print("count",count,"keys",resp.keys())
            if count in resp.keys():
                resp[count] = resp[count] + [tmp.val]
            else:
                resp[count] = [tmp.val]
            count +=1
            if tmp.left:
                q.append([tmp.left,count])
            if tmp.right:
                q.append([tmp.right,count])
            if len(q) >0:
                tmp_val = q.pop(0)
                tmp = tmp_val[0]
                count = tmp_val[1]
            else:
                tmp = None
        resp1 = []
        print(resp)
        j = sorted(resp.keys())
        resp1 = [resp[i] for i in j]
        print(resp1)
        return resp1
