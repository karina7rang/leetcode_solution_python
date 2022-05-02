class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex==0: return [1]
        elif rowIndex==1: return [1,1]
        else:
            res = [1,1]
            for i in range(2,rowIndex+1):
                for j in range(i-1):
                    res[j]=res[j]+res[j+1]
                res.insert(0,1)
                # print(res)
            return res

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = []
        for i in range(rowIndex+1):
            tmp = [1]*(i+1)
            for j in range(1,i):
                tmp[j] = pre[j-1]+pre[j]
            pre = tmp
        return tmp