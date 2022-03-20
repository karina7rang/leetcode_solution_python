class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        for i in range(numRows):
            # print(res)
            if i ==0: res.append([1])
            elif i==1: res.append([1,1])
            else:
                tmp = []
                for j in range(i+1):
                    if j==0: tmp.append(1)
                    elif j==i: tmp.append(1)
                    else:
                        tmp.append(res[i-1][j-1]+res[i-1][j])
                res.append(tmp)
        
        return res

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = [1]*(i+1)
            for j in range(1,i):
                tmp[j]=res[i-1][j-1]+res[i-1][j]
            res.append(tmp)
        return res