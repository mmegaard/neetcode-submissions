class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and nums[i - 1] == val:
                continue
            last_i = i
            l = i + 1
            r = len(nums) - 1
            while l < r:
                result = nums[l] + nums[r]
                left = nums[l]
                right = nums[r]
                if result + nums[i] == 0:
                    print('the indexes', i, l, r)
                    sums.append([nums[l],nums[r],nums[i]])
                    while l < r and nums[l] == left:
                        l += 1
                elif result + nums[i] > 0:
                    while r > l and nums[r] == right:
                        r -= 1
                else:
                    while l < r and nums[l] == left:
                        l += 1
        return sums
        