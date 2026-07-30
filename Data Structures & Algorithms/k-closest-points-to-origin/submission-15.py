class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #maintain a minHeap of size 2, keep the 2 lowest at all times
        minHeap = []
        res = []
        for x, y in points:
            dist = x **2 + y**2
            minHeap.append([dist,x,y])
        heapq.heapify(minHeap)
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1

        return res