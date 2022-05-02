# https://leetcode.com/problems/longest-common-prefix/

# O(n+m)
class Solution1:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0]
        if len(strs)>1:
            for istr in strs[1:]:
                lookup=True
                end = len(prefix)
                while (end>0) & (lookup==True):
                    if prefix[:end] == istr[:end]:
                        lookup=False
                    else:
                        end -= 1
                        prefix = prefix[:end]
        return prefix

# O(n+m)
class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0: return ''
        elif len(strs)==1: return strs[0]
        else:
            res = strs[0]
            if res=='': return res
            for istr in strs[1:]:
                if istr=='': return ''
                j=0
                threshold = min(len(res)-1, len(istr)-1)
                while res[j]==istr[j]:
                    if j<threshold: j+=1
                    else: 
                        j+=1 
                        break
                res = res[:j]
                if res=='': return res
                        
        return res

test_cases = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    ['hello'],
    ['wow',''],
    ["flower","flower","flower","flower"],
    ["abb","abc"],
    ["ab", "a"],
]

for i in test_cases:
    res = Solution1().longestCommonPrefix(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().longestCommonPrefix(i)
    print(res)