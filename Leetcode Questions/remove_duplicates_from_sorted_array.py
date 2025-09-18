class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count=1
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[count]=nums[j]
                count+=1
        return count
