class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        concat = [0] * (2 * length)
        for i,num in enumerate(nums):
            concat[i] = num
            concat[i + length] = num
        return concat