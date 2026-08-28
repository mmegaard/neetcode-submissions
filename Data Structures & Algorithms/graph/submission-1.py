class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        for edge in self.graph[src]:
            if edge == dst:
                self.graph[src].remove(edge)
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        queue = collections.deque()
        visit = set()
        queue.append(src)
        visit.add(src)
        while queue:
            dist = len(queue)
            for _ in range(dist):
                key = queue.popleft()
                if key == dst:
                    return True
                edges = self.graph[key]
                for edge in edges:
                    if edge not in visit:
                        
                        visit.add(edge)
                        queue.append(edge)
        return False
