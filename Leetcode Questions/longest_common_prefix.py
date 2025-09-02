from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest, largest = min(strs), max(strs)
        for i, ch in enumerate(smallest):
            if ch != largest[i]:
                return smallest[:i]
        return smallest
