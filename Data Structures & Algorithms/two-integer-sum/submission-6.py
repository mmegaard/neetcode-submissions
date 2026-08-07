class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            looking_for = target - num
            if looking_for in hashmap:
                return [hashmap[looking_for], index]
            hashmap[num] = index
