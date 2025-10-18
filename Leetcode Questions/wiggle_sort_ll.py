class Solution:
    def wiggleSort(self, nums):
        
        nums.sort()
        
        
        n = len(nums)
        mid = (n + 1) // 2  
        small = nums[:mid] 
        large = nums[mid:]
        
        
        nums[::2] = small[::-1]  
        nums[1::2] = large[::-1] 
