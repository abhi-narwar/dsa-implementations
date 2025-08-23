class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:   # check if already seen
                return True
            hashset.add(n)     # store in set
        return False
