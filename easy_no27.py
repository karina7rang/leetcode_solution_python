# https://leetcode.com/problems/remove-element/

class Solution1:
    def removeElement(self, nums, val):
        idx = 0
        while idx<len(nums):
            if nums[idx]==val:
                nums.remove(nums[idx])
            else:
                idx+=1


class Solution2:
    def removeElement(self, nums, val):
        i = 0
        while i<len(nums):
            if nums[i]==val: nums.pop(i)
            else:
                i+=1

test_cases = [
    [[3,2,2,3],3],
    [[0,1,2,2,3,0,4,2],2],
    [[],0],
]

for i,j in test_cases:
    res = Solution1().removeElement(i,j)
print(test_cases)
print('------------------')

test_cases = [
    [[3,2,2,3],3],
    [[0,1,2,2,3,0,4,2],2],
    [[],0],
]

for i,j in test_cases:
    res = Solution2().removeElement(i,j)
print(test_cases)