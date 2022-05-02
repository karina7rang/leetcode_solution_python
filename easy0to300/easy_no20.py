# https://leetcode.com/problems/valid-parentheses/

class Solution1:
    def isValid(self, s: str) -> bool:
        lspair = {')':'(', ']':'[', '}':'{'}
        ls = []
        for i in s:
            if i in lspair.values():
                ls.append(i)
            else:
                if not ls: return False
                if ls.pop()!=lspair[i]:
                    return False
        if ls: 
            return False
        else: 
            return True
        


class Solution2:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[','}':'{'}
        tmp = []
        for i in s:
            if i not in mapping: 
                tmp.append(i)
            else:
                if not tmp: return False
                if tmp.pop()!=mapping[i]: return False
        if tmp:return False
        else:return True

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "((()",
    "",
    "([)]",
    "])",
    "]",
]

for i in test_cases:
    res = Solution1().isValid(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().isValid(i)
    print(res)