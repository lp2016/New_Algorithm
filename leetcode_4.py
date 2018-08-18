class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L1=len(nums1)
        L2=len(nums2)
        if L1 == 1 and L2 == 1:
            return (nums1[0]+nums2[0])/2
        if L1 %2 ==0:
            mid1=(nums1[L1//2]+nums1[L1//2-1])/2
            index1=L1//2-1
        else:
            mid1=nums1[L1//2]
            index1=L1//2
        if L2 %2 ==0:
            mid2=(nums2[L2//2]+nums2[L2//2-1])/2
            index2=L2//2-1
        else:
            mid2=nums2[L2//2]
            index2=L2//2
        if mid1 == mid2 :
            return mid1
        elif mid1> mid2:
            return self.findMedianSortedArrays(nums1[:index1+1],nums2[index2+1:])
        else:
            return self.findMedianSortedArrays(nums1[index1+1:],nums2[:index2+1])

print(Solution().findMedianSortedArrays([1,2],[3]))