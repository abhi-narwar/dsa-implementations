class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        i=1
        for j in range(1,n):
            if nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i+=1
        return i
    



        

        