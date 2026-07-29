class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        #now a max stones, min stones with negatives
#    6
#  3   4                     
#2 2

#    3
#  2   2
#2
 
#    1
#. 2.   2

#.  1
# 2

# 1
        #now the heaviest stone is on top.
        index = 0
        while len(stones) > 1:
            first = heapq.heappop(stones)
            #largest child
            second = heapq.heappop(stones)
            # if second is the more negative number, then smash
            if second > first:
                print('second', second, 'first', first)
                heapq.heappush(stones, first - second)
        print(stones)
        return -stones[0] if len(stones) > 0 else 0