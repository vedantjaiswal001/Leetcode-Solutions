class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]

        ans=[[1],[1,1]]
        give=[]
        sumi=0
        for i in range(3,numRows+1):
            x=ans[-1]
            z=x.copy()
            j=0
            k=1
            while k<len(ans[-1]):
                sumi=x[j]+x[k]
                z[k]=sumi
                j=j+1
                k=k+1
                if k==len(ans[-1]):
                    z.append(1)
            ans.append(z)
            sumi=0
        
        return ans    