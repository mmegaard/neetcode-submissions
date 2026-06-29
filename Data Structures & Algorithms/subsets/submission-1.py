class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = [[]]

        #DO THE ITERATIVE NEEDFUL

        for num in nums:
            combos += [subset + [num] for subset in combos]
        return combos
