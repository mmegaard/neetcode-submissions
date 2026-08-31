"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copymap = {}
        queue = collections.deque()
        queue.append(node)
        while queue:
            curnode = queue.popleft()
            if curnode not in copymap:
                copymap[curnode] = Node(curnode.val)
            neigbs = []
            for neighbor in curnode.neighbors:
                if neighbor not in copymap:
                    copymap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                neigbs.append(copymap[neighbor])
            copymap[curnode].neighbors = neigbs
        return copymap[node]
                    
            



            