# https://leetcode.com/problems/implement-strstr/

class Solution1:
    def strStr(self, haystack, needle):
        if needle=='': 
            return 0
        elif haystack=='': 
            return -1
        else:
            for idx in range(len(haystack)):
                # print(idx, haystack[idx:len(needle)])
                if haystack[idx:(idx+len(needle))]==needle:
                    return idx
            return -1        
                


class Solution2:
    def strStr(self, haystack, needle):
        if needle=='': return 0
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:(i+n)]==needle: return i
        return -1

test_cases = [
    ['hello','ll'],
    ['aaaaa','bba'],
    ['',''],
    ['','a'],
]

for i,j in test_cases:
    res = Solution1().strStr(i,j)
    print(res)
print('------------------')
for i,j in test_cases:
    res = Solution2().strStr(i,j)
    print(res)