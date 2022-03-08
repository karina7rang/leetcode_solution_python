# https://leetcode.com/problems/add-binary/

class Solution1:
    def addBinary(self,a,b):
        res = str(int(a) + int(b))
        res = [int(i) for i in res]
        idx = len(res)-1
        pre = 0
        while idx>=0:
            res[idx] = res[idx] + pre
            if res[idx]==2:
                pre = 1
                res[idx] = 0
            elif res[idx]>2:
                pre = 1
                res[idx] = 1
            else:
                pre = 0
            idx-=1
        if pre>0: res = [pre] + res
        res = [str(i) for i in res]
        return ''.join(res)


class Solution3:
    def addBinary(self,a,b):
        a = int(a,2)
        b = int(b,2)
        return bin(a+b)[2:]

test_cases = [
    ["11","1"], # 100
    ['1010','1011'], # 10101
    ['111','111'], # 1110
    ['11111','11111'], # 111110

]

for i,j in test_cases:
    res = Solution1().addBinary(i,j)
    print(res)
print('------------------')
for i,j in test_cases:
    res = Solution3().addBinary(i,j)
    print(res)