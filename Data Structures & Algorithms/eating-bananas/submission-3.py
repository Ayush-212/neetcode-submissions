class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        def can_eat(k:int)->bool:
            hours_needed = 0
            for pile in piles:
                hours_needed+=math.ceil(pile/k)
            return hours_needed<=h

        while low<=high:
            mid = (low+high)//2
            if can_eat(mid):
                ans = mid
                high = mid -1
            else:
                low = mid+1
        return ans