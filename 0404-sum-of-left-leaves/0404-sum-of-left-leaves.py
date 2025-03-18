class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum_left_leaves = 0

        # Check if the left child is a leaf
        if root.left and not root.left.left and not root.left.right:
            sum_left_leaves += root.left.val

        # Recursively call for the left and right subtrees
        sum_left_leaves += self.sumOfLeftLeaves(root.left)
        sum_left_leaves += self.sumOfLeftLeaves(root.right)

        return sum_left_leaves
