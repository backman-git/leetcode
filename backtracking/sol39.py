class Solution(object):




    def reject(self,l,target):

        if sum(l) >target:
            return True
        return False

    def accept(self,l,target):
        return sum(l)== target



    def BK(self,l,target,candidates):



        if self.reject(l,target):
            return

        if self.accept(l,target):
            self.res.append(l)




        for pL in self.gen(l,candidates):
            self.BK(pL,target,candidates)



    def gen(self,l,candidates):

        for d in candidates:
            if len(l)==0:
                yield [d]
            elif l[-1] <=d:
                yield l+[d]







    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]

        self.BK([],target,candidates)
        return self.res


sol = Solution()

print sol.combinationSum([2,3,6,7],7)



