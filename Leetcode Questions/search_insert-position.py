from typing import List             
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                e = mid - 1
            else:
                s = mid + 1

        return s 
