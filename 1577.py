class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def addToCount(nums1, nums2):
            dic = {}
            res = 0
            for num in nums1:
                if num ** 2 in dic:
                    dic[num ** 2] += 1
                else:
                    dic[num ** 2] = 1
                    
            for i in range(len(nums2)):
                for j in range(i+1, len(nums2)):
                    if nums2[i] * nums2[j] in dic:
                        res += dic[nums2[i] * nums2[j]]
            return res
        return addToCount(nums1, nums2) + addToCount(nums2, nums1)