from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left= 0
        right=len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1  # go right
            else:
                right = mid     # go left (or mid)
        
        return left  # or right (both same)

