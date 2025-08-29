from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        
        while s <= e:
            mid = (s + e) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                e = mid - 1
            else:
                s = mid + 1
        
        return -1  
