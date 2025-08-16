class Solution:
    def countDigit(self, n):
        count = 0
        while n > 0:
            r = n % 10   
            count += 1   
            n = n // 10  
        return count
obj = Solution()
print(obj.countDigit(3456789))  
