class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower().replace(' ','') if i.isalpha() | i.isdigit()]
        if s==s[::-1]:
            return True
        else:
            False

class Solution:
    def wow(self, s):
        s = s.lower()
        s = [i for i in s if i.isalpha() | i.isdigit()]
        return s==s[::-1]