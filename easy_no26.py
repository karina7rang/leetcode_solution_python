# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution1:
    def removeDuplicates(self, nums) -> int:
        n=k=len(nums)
        pre = None
        idx = 0
        while idx<k:
            cur = nums[idx]
            if cur==pre:
                del nums[idx]
                k-=1
            else:
                pre = cur
                idx+=1
        # nums+=['b']*(n-k)
        return k

class Solution2:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n<2: return n
        i=1
        while i<len(nums):
            if nums[i-1]==nums[i]: 
                nums.pop(i-1)
            else:
                i+=1

test_cases = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4],
    [1],
    [1,1,1,1],
]

for i in test_cases:
    res = Solution1().removeDuplicates(i)
    print(i)
print('------------------')

test_cases = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4],
    [1],
    [1,1,1,1],
]

for i in test_cases:
    res = Solution2().removeDuplicates(i)
    print(i)