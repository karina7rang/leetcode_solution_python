# https://leetcode.com/problems/palindrome-number/

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        flag = True
        idx = 0
        n = len(strx)
        if n==1: return flag
        while (flag)&(idx<n//2):
            # print(strx,strx[idx],strx[n-idx-1])
            flag = strx[idx]==strx[n-idx-1]
            idx +=1
        return flag

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        backx = strx[::-1]
        return strx==backx

test_cases = [
    121,
    -121,
    10,
    123,
    1000,
    1001,
]

for i in test_cases:
    res = Solution1().isPalindrome(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().isPalindrome(i)
    print(res)