from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,target):
            left=0
            right=len(nums)-1
            first=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    first=mid
                    right=mid-1 #check left side 
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return first


        def Last(nums,target):
            left=0
            right=len(nums)-1
            Last=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    Last=mid
                    left=mid+1 #check right side 
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return Last
        return [first(nums,target),Last(nums,target)]
