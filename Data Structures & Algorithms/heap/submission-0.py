class MinHeap:

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
            
    def pop(self) -> int:
        #remove the lowest
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        top = self.top()
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return top

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)

    def _bubble_up(self, index):
        parent = index // 2
        #at index, find parent, is it bigger? swap
        while index > 1 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2

    def _bubble_down(self, index):
        # find smaller of the two childeren at index
        child = index * 2
        while child < len(self.heap):
            #if right is in bounds and also is smaller than left
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1
            #if child is not smaller than parent, stop
            if self.heap[child] >= self.heap[index]:
                return
            
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = index * 2

        