class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for index, num in enumerate(nums):
            if num == val:
                for i in range(index + 1, len(nums)):
                    if nums[i] != val:
                        nums[index] = nums[i]
                        nums[i] = val
                        break

        count = 0
        for num in nums:
            if num != val:
                count += 1
        return count