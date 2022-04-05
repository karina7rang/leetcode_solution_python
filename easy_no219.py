class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checklist = {}
        for i in range(len(nums)):
            if nums[i] in checklist:
                if abs(checklist[nums[i]]-i)<=k:
                    return True
                else:
                    checklist[nums[i]] = i
            else:
                checklist[nums[i]] = i
        return False