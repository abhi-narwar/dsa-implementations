from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If only one string, return it directly
        if len(strs) == 1:
            return strs[0]

        # Take the first string as initial prefix
        prefix = strs[0]

        # Compare prefix with each string in the list
        for s in strs[1:]:
            # While current string doesn't start with prefix, reduce prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last character
                if prefix == "":
                    return ""  # no common prefix
        
        return prefix
