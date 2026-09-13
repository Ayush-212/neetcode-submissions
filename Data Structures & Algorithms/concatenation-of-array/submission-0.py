class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        arr = [0]*(2*n)
        for i in range(0,n):
            arr[i] = nums[i]
            arr[n+i] = nums[i]
        return arr