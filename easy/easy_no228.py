class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [f"{nums[0]}"]
        res = [[nums[0],nums[0]]]
        for i in range(1, len(nums)):
            if (nums[i]-nums[i-1])==1:
                res[-1][1] = nums[i]
            else:
                res.append([nums[i],nums[i]])
        
        for i in range(len(res)):
            if res[i][0]==res[i][1]:
                res[i] = f"{res[i][0]}"
            else:
                res[i] = f"{res[i][0]}->{res[i][1]}"
        return res
                

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [f"{nums[0]}"]
        res = [[nums[0]]]
        for i in range(1, len(nums)):
            if (nums[i]-nums[i-1])==1:
                res[-1] = [res[-1][0],nums[i]]
            else:
                res.append([nums[i]])
        
        for i in range(len(res)):
            if len(res[i])==1:
                res[i] = f"{res[i][0]}"
            else:
                res[i] = f"{res[i][0]}->{res[i][1]}"
        return res
                

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        res = []
        s = e = str(nums[0])
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1])==1:
                e = str(nums[i])
            else:
                if s==e:
                    res.append([s])
                else:
                    res.append([s,e])
                s = e = str(nums[i])
        if s==e:
            res.append([s])
        else:
            res.append([s,e])
                
        return ['->'.join(i) for i in res]