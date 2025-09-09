class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        else:
            return -1
        