class Solution:
    def titleToNumber(self, s: str) -> int:
        dictionary = {}
        
        for i in range(97,124):
            dictionary[chr(i).upper()] = i-96
        # print(dictionary)

        res = 0
        loop = 0
        for i in s[::-1]:
            res += dictionary[i]*(26**loop)
            loop+=1


        return res

        
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res*26 + (ord(i)-64)
        return res