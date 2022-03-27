class Solution:
    def isHappy(self, n: int) -> bool:

        
        checklist = []
        res = None
        number = n
        while res==None:
            
            if number==1: 
                res=True
            elif number in checklist: 
                res=False
            else:
                checklist.append(number)
                number = sum([int(i)**2 for i in list(str(number))])
                
        return res

class Solution:
    def isHappy(self, n: int) -> bool:
        pool = set()
        while n!=1:
            n = sum([int(i)**2 for i in str(n)])
            if n in pool:
                return False
            else:
                pool.add(n)
        return True

class Solution:
    def isHappy(self, n: int) -> bool:
        pool = []
        while n!=1:
            n = sum([int(i)**2 for i in str(n)])
            if n in pool:
                return False
            else:
                pool.append(n)
        return True