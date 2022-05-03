class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.dfs(sorted(candidates), target, [], res)
        return res
    
    def dfs(self, nums, target, path, res):
        if target<0:
            return
        elif target==0:
            if path not in res:
                res.append(path)
            return
        else:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], target-nums[i], path+[nums[i]], res)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
    
    def dfs(self, nums, target, start, path, res):
        if target<0:
            return
        elif target==0:
            res.append(path)
            return
        else:
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                else:
                    self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
                