class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        res = x
        for i in range(abs(n)-1):
            res=res*x
        if n>0:
            return res
        if n<0:
            return 1/res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def myfunc(num, power):
            if power==0:
                return 1
            elif power%2==0:
                return myfunc(num*num, power//2)
            else:
                return num*myfunc(num*num, (power-1)//2)
        
        if n>=0:
            return myfunc(x, abs(n))
        if n<0:
            return 1/myfunc(x, abs(n))
                