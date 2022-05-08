class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, options, path, res):
        if len(options)>0:
            for idx in range(len(options)):
                self.dfs(options[:idx]+options[idx+1:], path+[options[idx]], res)
        else:
            if path not in res:
                res.append(path)


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.dfs(sorted(nums), [], res)
        return res
    
    def dfs(self, options, path, res):
        if len(options)>0:
            for idx in range(len(options)):
                if idx>0 and options[idx]==options[idx-1]:
                    continue
                else:
                    self.dfs(options[:idx]+options[idx+1:], path+[options[idx]], res)
        else:
            res.append(path)