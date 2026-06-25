# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        min_val = root.val

        def findSmallest(root: Optional[TreeNode], k: int):
                nonlocal count, min_val
                if not root:
                    return
                findSmallest(root.left, k)
                if count == k:
                    return
                count+= 1
                if count == k:
                    min_val = root.val
                    return
                findSmallest(root.right, k)
                
        findSmallest(root, k)
        return min_val
        