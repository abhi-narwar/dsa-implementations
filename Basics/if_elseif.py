class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("A")
        elif marks >= 70:
            print("B")
        elif marks >= 50:
            print("C")
        elif marks >= 35:
            print("D")
        else:
            print("Fail")

3
marks = int(input())

s = Solution()
s.studentGrade(marks)
