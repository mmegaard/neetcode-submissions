# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.traverse(root) >= 0

    def traverse(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.traverse(root.left) 
        if left == -1:
            return - 1
        right = self.traverse(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

        

            