class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}  # Stores: num -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
