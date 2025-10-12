class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i+1]=nums[j]
                i+=1
        return i+1
        
