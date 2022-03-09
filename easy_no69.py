# https://leetcode.com/problems/sqrtx/

# O(n)
class Solution1:
    def mySqrt(self,x):
        # if x<2: return x
        i = 0
        while i<=x:
            if i*i==x:
                return i
            if i*i > x:
                return i-1
            i+=1
        return max(i,x)


class Solution2:
    def mySqrt(self,x):
        if x<2: return x

        s=0
        e=x
        while s<e:
            # print(s,e)
            mid = s+(e-s)//2
            # print(s,e,mid)
            if mid**2<x:
                s=mid+1
            elif mid**2==x:
                return mid
            else:
                e=mid-1
        
        if s**2<=x: return s
        else: return s-1

test_cases = [
    4,
    8,
    9,
    6,
    0,
    1,
    2,
    3,
]

for i in test_cases:
    res = Solution1().mySqrt(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().mySqrt(i)
    print(res)