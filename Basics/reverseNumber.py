class Solution:
    def reverseNumber(self, n):
        rev = 0
        while n > 0:
            digit = n % 10       
            rev = rev * 10 + digit 
            n = n // 10        
        return rev
obj = Solution()
print(obj.reverseNumber(12345)) 
