class Solution:
    def isPalindrome(self, n):
        original = n
        rev = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n = n // 10
        return original == rev



n = int(input("Enter a number: "))


sol = Solution()

if sol.isPalindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome number")
