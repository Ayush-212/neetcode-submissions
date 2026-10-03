class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num-1) not in num_set:
                current_n = num
                c_streak = 1
                while(current_n+1) in num_set:
                    current_n += 1
                    c_streak += 1
                longest = max(longest, c_streak)
                
        return longest