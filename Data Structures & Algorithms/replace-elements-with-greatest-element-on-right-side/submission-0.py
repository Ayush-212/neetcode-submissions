class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = 1
        for i in range(len(arr)-1,-1,-1):
            new = max(maxVal, arr[i])
            arr[i] = maxVal
            maxVal = new
        arr[len(arr)-1] = -1
        return arr