class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        key = []
        dup = []
        for i in nums:
            if i not in key:
                key.append(i)
            else:
                dup.append(i)
        
        return list(set(key)-set(dup))[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = {}
        for i in nums:
            if i in check:
                del check[i]
            else:
                check[i]=0
        return list(check.keys())[0]