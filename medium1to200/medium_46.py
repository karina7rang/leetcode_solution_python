class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.findcombo(nums, [], res)
        return res
    
    def findcombo(self, options, path, res):
        if len(options)>0:
            for i in range(len(options)):
                self.findcombo(options[:i]+options[i+1:], path+[options[i]], res)
        else:
            res.append(path)