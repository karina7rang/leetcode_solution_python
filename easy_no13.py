# https://leetcode.com/problems/roman-to-integer/

# O(n)
class Solution1:
    def romanToInt(self, s: str) -> int:
        convertmap = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        resnum = 0
        n = len(s)
        for i in range(n):
            istr = s[i]
            inum = convertmap[istr]
            if i!=n-1:
                nextnum = convertmap[s[i+1]]
                if inum<nextnum:
                    resnum -= inum
                else:
                    resnum += inum
            else:
                resnum += inum
        return resnum

# O(n)
class Solution2:
    def romanToInt(self, s: str) -> int:
        r2num = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

        if len(s)==0: return 0
        elif len(s)==1: return r2num[s]
        else:
            tt = 0
            for i in range(len(s)-1):
                inum = r2num[s[i]]
                inum_next = r2num[s[i+1]]
                if inum<inum_next:
                    tt -= inum
                else:
                    tt += inum
            tt +=r2num[s[len(s)-1]]
            return tt

test_cases = [
    '',
    'III',
    'IX',
    'LVIII',
    'MCMXCIV',
]

for i in test_cases:
    res = Solution1().romanToInt(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().romanToInt(i)
    print(res)