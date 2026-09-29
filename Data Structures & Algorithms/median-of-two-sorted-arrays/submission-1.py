class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth(a,m,b,n,k,astart,bstart):
            if m > n:
                return get_kth(b,n,a,m,k,bstart,astart)
            if m == 0:
                return b[bstart + k - 1]
            if k == 1:
                return min(a[astart], b[bstart])
            
            p = min(m, k//2)
            q = min(n, k//2)

            if a[astart + p - 1] > b[bstart + q - 1]:
                return get_kth(a,m,b,n-q,k-q,astart,bstart+q)
            else:
                return get_kth(a,m-p,b,n,k-p,astart+p,bstart)
        
        first = (len(nums1)+len(nums2)+ 1)//2
        second = (len(nums1)+len(nums2)+ 2)//2
        return (get_kth(nums1,len(nums1),nums2,len(nums2),first,0,0) + get_kth(nums1,len(nums1),nums2,len(nums2),second,0,0)) / 2.0
