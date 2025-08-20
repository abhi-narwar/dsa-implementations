
#Boyer-Moore Voting Algorithm


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
    
    
    
#using hashmap
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        for num, freq in count.items():
            if freq > n // 2:
                return num


