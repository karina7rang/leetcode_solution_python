class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for w in strs:
            key = ''.join(sorted(w))
            if key in res:
                res[key] += [w]
            else:
                res[key] = [w]
        return res.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for w in strs:
            key = tuple(sorted(w))
            if key in res:
                res[key] += [w]
            else:
                res[key] = [w]
        return res.values()