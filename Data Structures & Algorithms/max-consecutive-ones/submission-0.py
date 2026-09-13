class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0

        for num in nums:
            if num == 1:
                current +=1
            if num == 0:
                current = 0
            if max < current:
                max = current
        return max