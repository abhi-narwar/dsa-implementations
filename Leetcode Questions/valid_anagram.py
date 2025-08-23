class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create two dictionaries to count frequency of each character
        countS, countT = {}, {}
        
        # Step 3: Count characters of both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # increase count for s
            countT[t[i]] = 1 + countT.get(t[i], 0)  # increase count for t
        
        # Step 4: Compare the two frequency dictionaries
        return countS == countT
