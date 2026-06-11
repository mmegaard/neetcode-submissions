class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchRec(nums, target ,0, len(nums) - 1)
    def searchRec(self, nums: List[int], target: int, s, e) -> int:
        mid = (s + e) // 2
        if s > e:
            return -1
        elif nums[mid] == target:
            return mid
        elif s == e:
            return -1
        elif nums[mid] > target:
            return self.searchRec(nums, target, s, mid - 1)
        elif nums[mid] < target:
            return self.searchRec(nums, target, mid + 1, e)
        else:
            return -1