class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        knums = []
        heapq.heapify(knums)
        for num in nums:
            heapq.heappush(knums, num)
            if len(knums) > k:
                heapq.heappop(knums)
        return heapq.heappop(knums)