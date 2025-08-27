from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)  # key: sorted word, value: list of anagrams

        for word in strs:
            key = ''.join(sorted(word))  # sort the letters to form key
            anagrams[key].append(word)

        return list(anagrams.values())
