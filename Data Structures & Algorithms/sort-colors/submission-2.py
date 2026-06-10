class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        for num in nums:
            arr[num] += 1
        
        num_i = 0
        for i in range(len(arr)):
            for _ in range(0, arr[i]):
                nums[num_i] = i
                num_i += 1
        return nums