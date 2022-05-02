# https://leetcode.com/problems/two-sum/

# O(n)
class Solution1:
    def twoSum(self, nums, target):
        for i1 in range(len(nums)):
            num2 = target - nums[i1]
            if num2 in nums:
                i2 = nums.index(num2)
                if i1!=i2:
                    if nums[i1]+nums[i2]==target: 
                        return [i1, i2]
# O(n^2)
class Solution2:
    def twoSum(self, nums, target):
        n = len(nums)
        for i1 in range(n):
            for i2 in range(n):
                if (i1!=i2) & (nums[i1]+nums[i2]==target):
                    return [i1, i2]


test_cases = [
    [[2,7,11,15], 9],
    [[3,2,4], 6],
    [[3,3], 6],
]
for i,j in test_cases:
    res = Solution2().twoSum(i,j)
    print(res)