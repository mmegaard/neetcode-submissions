import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #for each pile, figure out the most efficient way to get through bananas.
        # divde the total number of banans by k to figure out how many hours
        max_banana = None
        for pile in piles:
            if not max_banana or max_banana < pile:
                max_banana = pile
        print('max is', max_banana)
        start = 1
        finish = max_banana
        closest_rate = max_banana
        while start <= finish:
            rate = start + (finish - start) // 2
            rate_sum = 0
            for pile in piles:
                #print('for pile', pile, 'with rate', rate, 'would take', math.ceil(pile/rate))
                rate_sum += math.ceil(pile/rate)
            print('got rate_sum', rate_sum, 'for rate', rate, 'with diff',  h - rate_sum)
            if h - rate_sum < 0:
                #if sum is lower than the hours, see if we can go higher
                start = rate + 1
               
            elif h - rate_sum >= 0:
                finish = rate - 1
                closest_rate = rate
            else:
                return rate
            
        return closest_rate

        #for the search range of 0 to hours, check in the array how lo
    
        #[1,4,3,2]
        # at 1 bannana per hour it's 10
        # at 2 banana per hour it's 1 + 2 + 2 + 1 = 6
        # at 3 banana per hour it's 1 + 2 + 1 + 1 = 5