# https://leetcode.com/problems/climbing-stairs/

# O(n**2)
class Solution1:
    def climbStairs(self,n):
        def climb(rest):
            if rest<=1:
                return 1
            else:
                return climb(rest-1) + climb(rest-2)
        return climb(n)

# O(n)
class Solution2:
    def climbStairs(self,n):
        ls = {}
        def climb(rest):
            if rest<=1:
                return 1
            else:
                if rest not in ls:
                    ls[rest] = climb(rest-1) + climb(rest-2)
                return ls[rest]    
        return climb(n)

# O(n)
class Solution3:
    def climbStairs(self,n):
        if n==1: return 1
        elif n==2: return 2
        tmp1=1
        tmp2=2
        for i in range(3,n+1):
            tmp = tmp1+tmp2
            tmp1 = tmp2
            tmp2 = tmp
        return tmp2

test_cases = [
    2,
    3,
    1,
    10,
]

for i in test_cases:
    res = Solution1().climbStairs(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().climbStairs(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution3().climbStairs(i)
    print(res)