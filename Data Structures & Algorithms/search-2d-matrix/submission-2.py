class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        low = 0
        high = m*n-1

        while low<=high:
            mid = low+(high-low)//2
            row = mid//n
            col = mid%n
            current = matrix[row][col]
            if current ==target:
                return True
            elif current<target:
                low=mid+1
            elif current>target:
                high = mid-1
        return False