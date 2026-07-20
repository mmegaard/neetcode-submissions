class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sort first so we can quit early
        #      2
        #    2   []
        #  2,[] 2 [] 
        #
        #
        #
        #
        nums.sort()
        result = []
        
        def dfs(i, combo, total):
            if total == target:
                result.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return
            combo.append(nums[i])
            #keep choosing the current number
            dfs(i,combo, total + nums[i])
            combo.pop()
            #skipping the current number
            dfs(i + 1,combo,total)
        
        dfs(0,[],0)
        return result