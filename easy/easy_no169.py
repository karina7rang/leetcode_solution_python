class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        
        myres = [k for k,v in sorted(mydict.items(), key=lambda i:i[1], reverse=True)]
        return myres[0]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ls = {}
        for i in nums:
            if i in ls:
                ls[i]+=1
            else:
                ls[i] = 1
        return [k for k, v in sorted(ls.items(), key=lambda item: item[1])][-1]