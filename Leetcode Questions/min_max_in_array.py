class Solution:
    def get_min_max(self, arr):
        min_val = float('inf')
        max_val = float('-inf')
        
        for i in arr:
            
            if i < min_val:
                min_val = i
            if i > max_val:
                max_val = i
                
        return min_val, max_val