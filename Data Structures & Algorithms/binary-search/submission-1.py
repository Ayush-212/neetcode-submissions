class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 1. Found the target
            if nums[mid] == target:
                return mid
            
            # 2. Check if the left half is normally sorted
            if nums[left] <= nums[mid]:
                # Is target inside this sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # Search left
                else:
                    left = mid + 1  # Search right
            
            # 3. Otherwise, the right half must be normally sorted
            else:
                # Is target inside this sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search right
                else:
                    right = mid - 1 # Search left
                    
        return -1 # Target not found
