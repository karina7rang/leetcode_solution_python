class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def myfunc(string):
            lsidx={}
            for i in range(len(string)):
                val = string[i]
                if val not in lsidx:
                    lsidx[val]=[i]
                else:
                    lsidx[val].append(i)
            return [j for i,j in lsidx.items()]
        
        return myfunc(s)==myfunc(t)