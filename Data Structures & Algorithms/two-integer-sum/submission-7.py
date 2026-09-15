class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in targetMap:
                return [targetMap[difference],index]
            else:
                targetMap[nums[index]] = index
        return []
