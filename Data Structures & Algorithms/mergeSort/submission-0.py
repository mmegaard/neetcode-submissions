# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelper(self, pairs: List[Pair], start:int, end:int):
        #find the base case which should be one node
        if end - start + 1 <= 1: 
            return pairs
        
        mid = (end + start) // 2

        self.mergeSortHelper(pairs, start, mid)
        self.mergeSortHelper(pairs, mid + 1, end)

        self.merge(pairs, start, mid, end)

        return pairs

    def merge(self, pairs: List[Pair], start:int, mid:int, end:int):
        #sorted left
        left = pairs[start:mid + 1]
        #sorted right
        right = pairs[mid + 1: end + 1]

        l = 0
        r = 0
        i = start

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[i] = left[l]
                l += 1
            else:
                pairs[i] = right[r]
                r += 1
            i += 1
        while l < len(left):
            pairs[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            pairs[i] = right[r]
            r += 1
            i += 1
         