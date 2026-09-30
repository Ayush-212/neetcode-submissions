class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j] == nums[i]:
                    return True
        return False
