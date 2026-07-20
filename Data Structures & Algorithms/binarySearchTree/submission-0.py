class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)
        if not self.root:
            self.root = node
            return
        
        cur = self.root
        while True:
            if key < cur.key:
                if not cur.left:
                    cur.left = node
                    return
                cur = cur.left
            elif key > cur.key:
                if not cur.right:
                    cur.right = node
                    return
                cur = cur.right
            else:
                cur.val = val
                return
        

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.findMin(self.root)
        if cur:
            return cur.val
        else:
            return -1

    def getMax(self) -> int:
        cur = self.root
        while cur:
            if cur.right:
                cur = cur.right
            else:
                return cur.val
        return -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node


    #remove node with key, return new root of subtree
    def removeHelper(self, cur, key) -> TreeNode:
        if cur == None:
            return None
        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if cur.left == None:
                return cur.right
            elif cur.right == None:
                return cur.left
            else:

                minNode = self.findMin(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        return cur


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
       
    
    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
            

