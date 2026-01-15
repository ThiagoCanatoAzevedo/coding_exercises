class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
    
solution = Solution()
print(solution.isPalindrome(121))

"""
Exercise annotations:
- Name: Palindrome Number
- Runtime: 4ms
- Memory: 12.36MB
"""