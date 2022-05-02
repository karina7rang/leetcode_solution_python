# https://leetcode.com/problems/merge-sorted-array/

# O(n*m)
class Solution1:
    def merge(self, nums1, m, nums2, n):
        for idx2 in range(n):
            for idx1 in range(m+n):
                if nums1[idx1]>=nums2[idx2]:
                    nums1.insert(idx1, nums2[idx2])
                    nums1.pop()
                    break
                else:
                    if idx1+1==m+n:
                        nums1.insert(m+idx2, nums2[idx2])
                        nums1.pop()


# O(n+m)
class Solution2:
    def merge(self, nums1, m, nums2, n):
        idx1 = 0
        idx2 = 0
        while idx1<(m+n) and idx2<n:
            if nums1[idx1]<nums2[idx2]:
                idx1+=1
            else:
                nums1.insert(idx1, nums2[idx2])
                nums1.pop()
                idx2+=1
                idx1+=1
        if idx1==m+n and idx2<n:
            nums1[-len(nums2[idx2:]):] = nums2[idx2:]


# O(log(n+m))
class Solution3:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m]+nums2)

test_cases = [
    [[1,2,3,0,0,0],3, [2,5,6],3],
    [[1],1, [],0],
    [[0],0, [1],1],
    [[1,1,4,0,0],3, [2,7],2],
    [[1,0],1,[2],1],
]

for i,m,j,n in test_cases:
    Solution1().merge(i,m,j,n)
    print(i)
print('------------------')

test_cases = [
    [[1,2,3,0,0,0],3, [2,5,6],3],
    [[1],1, [],0],
    [[0],0, [1],1],
    [[1,1,4,0,0],3, [2,7],2],
    [[1,0],1,[2],1],
]
for i,m,j,n in test_cases:
    Solution2().merge(i,m,j,n)
    print(i)

print('------------------')

test_cases = [
    [[1,2,3,0,0,0],3, [2,5,6],3],
    [[1],1, [],0],
    [[0],0, [1],1],
    [[1,1,4,0,0],3, [2,7],2],
    [[1,0],1,[2],1],
]
for i,m,j,n in test_cases:
    Solution3().merge(i,m,j,n)
    print(i)