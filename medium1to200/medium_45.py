class Solution:
    def jump(self, nums):
        
        maxidx = 0
        stepidx = 0
        minstep = 0
        for idx in range(len(nums)-1):
            maxidx = max(maxidx, idx+nums[idx])
            if maxidx>=(len(nums)-1):
                return minstep+1
            else:
                if idx>=stepidx:
                    minstep+=1
                    stepidx = maxidx
        return minstep

test_cases = [
[2,3,1,1,4], #2
[2,3,0,1,4], #2
[4,0,5,0,2,0,9,0,0,0,0,0,0,0,1], #3
[0], #0
[1], #0
[1,0], #1
[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3], #2
]
for i in test_cases:
    print(Solution().jump(i))
