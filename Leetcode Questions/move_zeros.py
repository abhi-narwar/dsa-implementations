class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
   
        for k in range(i, len(nums)):
            nums[k] = 0
            
