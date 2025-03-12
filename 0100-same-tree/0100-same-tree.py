# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:   #if both nodes are none, they are same
            return True

        if not p or not q:   #if only one has node, they are not same 
            return False 

        if p.val != q.val:    #if the values are different, they are not same
            return False 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
