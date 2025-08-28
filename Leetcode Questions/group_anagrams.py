class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # HashMap to store sorted string as key, and list of anagrams as value
        hashMap = {}

        # Loop through each word in the input list
        for s in strs:
            # Convert word to char array, sort it, then join back into string
            # Example: "eat" -> ['a','e','t'] -> "aet"
            charArray = sorted(s)
            sortedStr = "".join(charArray)

            # If the sorted word already exists in map, append current word
            if sortedStr in hashMap:
                listSubAnswer = hashMap[sortedStr]
                listSubAnswer.append(s)
            else:
                # Otherwise, create a new list with this word
                listSubAnswer = [s]
                hashMap[sortedStr] = listSubAnswer

        # Collect all grouped anagrams from the hashmap
        listAnswer = []
        for value in hashMap.values():
            listAnswer.append(value)

        # Return the final list of lists
        return listAnswer
