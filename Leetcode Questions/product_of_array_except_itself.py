class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Step 1: Create result array with 1s (will store prefix first)
        result = [1] * n
        
        # Step 2: Calculate prefix product for each index
        prefix = 1
        for i in range(n):
            result[i] = prefix   # store product of all left elements
            prefix *= nums[i]    # update prefix
        
        # Step 3: Multiply with suffix product
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix  # multiply with product of right elements
            suffix *= nums[i]    # update suffix
        
        return result