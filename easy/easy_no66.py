# https://leetcode.com/problems/plus-one/

class Solution1:
    def plusOne(self, digits):
        digits[-1] = digits[-1]+1
        i = len(digits)-1
        pre = 0
        while i>=0:
            new = digits[i]+pre
            if new<10:
                digits[i] = new
                break
            else:
                digits[i] = new-10
                pre = 1
                if i==0:
                    digits = [1]+digits
                i-=1
        return digits

class Solution2:
    def plusOne(self, digits):
        num = 0
        for i in digits:
            num = num*10+i
        num = num+1
        res = []
        for i in str(num):
            res.append(i)
        return res

test_cases = [
    [1,2,3],
    [4,3,2,1],
    [9],
    [9,9],
]

for i in test_cases:
    res = Solution1().plusOne(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().plusOne(i)
    print(res)