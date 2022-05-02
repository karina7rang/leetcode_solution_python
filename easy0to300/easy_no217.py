class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checklist = {}
        for inum in nums:
            if inum in checklist: 
                return True
            else:
                checklist[inum] = 0
        return False