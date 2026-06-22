# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack = []
        return_list = []
        while cur or stack:
            #go left as far as possible
            while cur:
                stack.append(cur)
                cur = cur.left
            #process leftmost null node's parent (the latest in the stack)
            cur = stack.pop()
            return_list.append(cur.val)
            #point check for right sibling
            cur = cur.right
        return return_list