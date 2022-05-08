class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i in range(1,len(num1)+1):
            for j in range(1,len(num2)+1):
                res+=  (10**(i-1))*int(num1[-i]) * (10**(j-1))*int(num2[-j])
        return str(res)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        power1 = 1
        for i in range(1,len(num1)+1):
            power2 = 1
            for j in range(1,len(num2)+1):
                res+=  power1*int(num1[-i]) * power2*int(num2[-j])
                power2*=10
            power1*=10
        return str(res)