class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        end = len(nums)
        while current < end:
            if nums[current] == val:
                end -= 1
                nums[current] = nums[end]
            else:
                current += 1
        return end

