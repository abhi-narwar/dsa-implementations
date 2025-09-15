class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i

        