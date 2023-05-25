class Solution:
    def countAndSay(self, n: int) -> str:
        y=n
        n=str(n)
        
        if str(n)=='1':
            return '1'
        ans=self.countAndSay(y-1)
        res=[]
        i=0
        
        while i<len(ans):
            count=0
            x=ans[i]
            
            while i<len(ans) and x==ans[i]:
                i+=1
                count+=1
        

            res.append(str(count))
            res.append(x)

        return ''.join(res)
	  
     
    
    
    