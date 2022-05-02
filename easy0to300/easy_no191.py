class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        b = str(bin(n))[2:]
        # print(n,bin(n), b)
        for i in b:
            if i=='1':
                res+=1
        
        return res

class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in bin(n) if i=='1'])
        