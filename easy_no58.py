# https://leetcode.com/problems/length-of-last-word/

class Solution1:
    def lengthOfLastWord(self,s):
        res = 0
        keepgoing = True
        for i in s[::-1]:
            if i!=' ':
                keepgoing=False
                res+=1
            else:
                if keepgoing==False:
                    break
        return res

class Solution2:
    def lengthOfLastWord(self,s):
        lss = s.split()
        if not lss: return 0
        else: return len(lss[-1])

class Solution3:
    def lengthOfLastWord(self,s):
        x = s.split(' ')
        x = [i for i in x if i]
        return len(x[-1])

test_cases = [
    'hello world',
    '   fly me  to    the moon  ',
    'fluffy is still joyboy',
    'a',
    '  s  ',
]

for i in test_cases:
    res = Solution1().lengthOfLastWord(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().lengthOfLastWord(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution3().lengthOfLastWord(i)
    print(res)