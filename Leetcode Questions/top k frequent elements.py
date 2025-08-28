from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        Function to return k most frequent elements from the list nums
        """
        
        # Step 1: Count how many times each number appears in nums
        # Example: nums = [1,1,1,2,2,3] -> freq = {1:3, 2:2, 3:1}
        freq = Counter(nums)
        
        # Step 2: Create "buckets" where index = frequency of numbers
        # Example: bucket[3] will have numbers appearing 3 times
        # We use len(nums)+1 because max frequency can be len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Place each number in the bucket corresponding to its frequency
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 4: Collect k most frequent elements
        result = []
        # Start from the back (highest frequency) and move to lower frequency
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:          # Take all numbers with this frequency
                result.append(num)         # Add number to result list
                if len(result) == k:       # Stop when we have collected k numbers
                    return result
