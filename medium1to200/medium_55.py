class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0: return False
        if n==1: return True
        lastvisit = 0
        for i in range(n-1):
            # print(i,lastvisit)
            if i <= lastvisit:
                lastvisit = max(lastvisit,i+nums[i])
                if lastvisit>=(n-1):
                    return True
            else:

                return False
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxidx = 0
        stepidx = 0
        for idx in range(len(nums)-1):
            maxidx = max(maxidx, idx+nums[idx])
            if maxidx>=(len(nums)-1):
                return True
            else:
                if idx>=stepidx:
                    if stepidx==maxidx:
                        return False
                    else:
                        stepidx = maxidx
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxidx = 0
        for idx in range(len(nums)-1):
            maxidx = max(maxidx, idx+nums[idx])
            if maxidx>=(len(nums)-1):
                return True
            else:
                if idx>=maxidx:
                    return False
        return True