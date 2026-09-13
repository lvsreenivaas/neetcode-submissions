class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles) + 1
        ans = end 
        while start <= end:
             mid_point = (start + end) // 2
             hours = sum(math.ceil(p / mid_point) for p in piles)
             if hours <= h:
                ans = mid_point
                end = mid_point - 1
             else:
                start = mid_point + 1
        return ans
                
