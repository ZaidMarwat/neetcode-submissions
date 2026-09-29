class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 1,3,5     2,4
        len1 = len(nums1)
        len2 = len(nums2)

        first = second = 0
        p,q = 0, 0

        for i in range((len1+len2)//2 + 1):
            if p < len1 and q < len2:
                if nums1[p] < nums2[q]:
                    second = first
                    first = nums1[p]
                    p += 1
                else:
                    second = first
                    first = nums2[q]
                    q += 1
            elif p < len1:
                second = first
                first = nums1[p]
                p += 1
            else:
                second = first
                first = nums2[q]
                q += 1
        
        if (len1 + len2) % 2:
            return float(first)
        
        return float((first + second)/2)


