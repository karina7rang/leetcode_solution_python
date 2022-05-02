class Solution:
    def convertToTitle(self, n: int) -> str:
        
        
        dictionary = {}
        
        for i in range(97,124):
            dictionary[i-96] = chr(i).upper()
        # print(dictionary)

        add = n%26
        remain = n//26
        if add==0:
            add=26
            remain-=1
        res = dictionary[add]

        while remain>0:
            add=remain%26
            if add==0:
                add=26
                remain-=1
            res=dictionary[add]+res
            remain = remain//26

        return res

class Solution:
    def convertToTitle(self, n: int) -> str:
        # A chr(65)
        res = ''
        while (n/26)>0:
            if n%26==0:
                res = 'Z'+res
                n=n//26-1
            else:
                res = chr(64+n%26)+res
                n=n//26
        return res