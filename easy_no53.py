# https://leetcode.com/problems/maximum-subarray/

# bad solution!!!
class Solution1:
    def maxSubArray(self, nums):
        return 0
        # n = len(nums)
        # if n==1: return nums[0]
        # ls = [None]*n
        # for i in range(n):
        #     ls[i] = sum(nums[:i+1])
        # low = min(ls)
        # high = max(ls[ls.index(low):])
        # print(ls)
        # # print(high, low)
        # if high==low:
        #     return max(nums)
        # else:
        #     return max(high,high-low)
            

class Solution2:
    def maxSubArray(self, nums):
        # if len(nums)==0: return ''
        elif len(nums)==1: return nums[0]

        curr = -float('inf')
        glob = -float('inf')
        for i in nums:
            curr = max(i, curr+i) # start or keep previous
            glob = max(curr, glob) # update best
        return glob

test_cases = [
    [-2,1,-3,4,-1,2,1,-5,4], #4,-1,2,1
    [1], #1
    [-1], #-1
    [5,4,-1,7,8], #5,4,-1,7,8
    [-1,4,-1,-1,-1,5,-1,-2], #4,-1,-1,-1,5
    [7,-1,-1], #7
    [0,1,7,-1], #1,7
    [-2,-1], #-1
    [-2,1], #1
    [-3,-2,-1], #-1
    [1,-1,-2], #1
    [0,-3,1,1], #1,1
    [1,1,-2], #1,1
]

for i in test_cases:
    res = Solution1().maxSubArray(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().maxSubArray(i)
    print(res)