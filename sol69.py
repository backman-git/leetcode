




class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        s1=set(nums1)
        s2=set(nums2)

        s3 = s1&s2

        return list(s3)


sol = Solution()


a=[1,2,3]
b=[1,2,3,4]
print sol.intersection(a,b)