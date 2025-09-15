class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != 0: 
                nums[i], nums[j] = nums[j], nums[i]  
                i += 1   
        
    
        for k in range(n):
            print(nums[k], end=" ")