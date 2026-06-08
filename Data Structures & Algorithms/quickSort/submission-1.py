# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]: 
        
        return self.quickSortHelper(pairs, 0, len(pairs))

    def quickSortHelper(self, pairs: List[Pair], s: int, e:int) -> List[Pair]: 
        length = e - s
        if length < 2:
            return pairs
        pivot = e - 1
        cur = s
        insert = s
        while cur < pivot:
            if pairs[cur].key < pairs[pivot].key:
                temp = pairs[cur]
                new = pairs[insert]
                pairs[insert] = temp
                pairs[cur] = new
                insert += 1
            cur += 1
        temp = pairs[insert]
        new = pairs[pivot]
        pairs[insert] = new
        pairs[pivot] = temp
        self.quickSortHelper(pairs, s, insert)
        self.quickSortHelper(pairs, insert + 1, e)
        return pairs


