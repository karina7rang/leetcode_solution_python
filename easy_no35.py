# https://leetcode.com/problems/search-insert-position/

# O(n)
class Solution1:
    def searchInsert(self, nums, target):
        for idx in range(len(nums)):
            if nums[idx]>=target:
                return idx
        return len(nums)

# O(logn)
class Solution2:
    def searchInsert(self, nums, target):
        idx = len(nums)//2
        if nums[0]>=target:
            return 0
        elif nums[-1]<target:
            return len(nums)

        while (idx>0) and (idx<len(nums)):
            if nums[idx]==target:
                return idx
            if nums[idx]>target:
                if nums[idx-1]<target: 
                    return idx
                else:
                    idx=idx//2
            else:
                if nums[idx+1]>=target: 
                    return idx+1
                else:
                    idx=idx+idx//2

test_cases = [
    [[1,3,5,6],5],
    [[1,3,5,6],2],
    [[1,3,5,6],7],
    [[1,3,5,6],0],
    [[1],3],
    [[4],3],
    [[1,3],2],
    [[1,2,3],2],
    [[1,3],3],
    [[1,2,3],3],
    [[1,2,3],1],
    [[1,4,6,7,8,9],6],
]

for i,j in test_cases:
    res = Solution1().searchInsert(i,j)
    print(res)
print('------------------')
for i,j in test_cases:
    res = Solution2().searchInsert(i,j)
    print(res)
