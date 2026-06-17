# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                #arrived at the deletion node
                temp = root
                temp_val = temp.val
                temp = temp.right
                while temp.left:
                    temp = temp.left
                temp_val = temp.val
                root.val = temp_val
                root.right = self.deleteNode(root.right, temp_val)
        return root
    
    

