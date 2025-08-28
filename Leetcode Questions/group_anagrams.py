from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where key = character count of a word, value = list of anagrams
        res = defaultdict(list)

        # Loop through every word in the input list
        for s in strs:
            # Create a list of 26 zeros for each alphabet letter (a to z)
            count = [0] * 26  

            # Count how many times each character appears in the word
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Use tuple(count) as a unique key (since lists can’t be keys in dict)
            res[tuple(count)].append(s)

        # Convert dict_values to list
        return list(res.values())