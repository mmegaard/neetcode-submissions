# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        return self.traverse(root, return_list)
    def traverse(self, root: Optional[TreeNode], return_list: List[int]) -> List[int]:
        if root == None:
            return return_list
        self.traverse(root.left, return_list)
        return_list.append(root.val)
        self.traverse(root.right, return_list)
        return return_list
