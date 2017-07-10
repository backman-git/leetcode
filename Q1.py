


#use internal Big Number library
def f(n):

    if n==0:
        return 0

    ary=[0]*(n+1)
    ary[1]=1

    for i in range(2,n+1):
        ary[i]=ary[i-1]+ary[i-2]

    return ary[n]


#==========================

# self-implementation Big Number add operation
import math
class BigN:

    def __init__(self,strs):
        self.val=[]
        if strs=="":
            return

        self.val.append( int(strs[:len(strs)%4]) ) if len(strs)%4 !=0 else None
        for idx in range(len(strs)%4,len(strs),4):
            self.val.append(int(strs[idx:idx+4]))

    @staticmethod
    def add(bigL,bigR):

        lV=bigL.val[:]
        rV=bigR.val[:]

        newN=BigN("")
        c=0
        while(len(lV) != 0 or len(rV)!=0):
            nR=lV.pop() if len(lV)!=0 else 0
            nL=rV.pop() if len(rV)!=0 else 0
            sumV=nR+nL+c
            n=(sumV)%10000
            newN.val=[n]+newN.val
            c=(sumV)/10000

        if c !=0:
            newN.val=[c]+newN.val
        return newN

    def stringify(self):

        return ''.join([str(v).zfill(4) if idx!=0 else str(v)  for idx,v in enumerate(self.val) ])

def f_big(n):

    if n==0:
        return 0

    ary=[BigN('0')]*(n+1)
    ary[1]=BigN('1')

    for i in range(2,n+1):
        ary[i]=BigN.add(ary[i-1],ary[i-2])

    return ary[n].stringify()

