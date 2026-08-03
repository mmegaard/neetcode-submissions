class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negatives = [-x for x in nums]
        heapq.heapify(negatives)
        for i in range(0,k - 1):
            heapq.heappop(negatives)
        
        top = heapq.heappop(negatives)
        return -top