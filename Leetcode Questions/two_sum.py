class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # store number -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [i,num_map[diff]]  # found the pair
            num_map[num] = i  # store index of current number
