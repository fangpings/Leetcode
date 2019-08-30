class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # len(nums1) <= len(nums2)
        # nums1 for i, m nums2 for j, n
        m, n = len(nums1), len(nums2)
        if not n:
            raise ValueError()
        if not m:
            if n % 2:
                return nums2[n//2]
            else:
                return (nums2[n//2] + nums2[n//2-1]) / 2
        l, r = 0, m
        mid = (m + n + 1) // 2
        even = not ((m + n) % 2)
        while l <= r:
            i = (l + r) // 2
            j = mid - i
            if i == 0:
                if nums2[j-1] <= nums1[i]:
                    if even:
                        if j == n:
                            return float((nums2[j-1] + nums1[i]) / 2)
                        else:
                            return float((nums2[j-1] + min(nums1[i], nums2[j])) / 2)
                    else:
                        return float(nums2[j-1])
                else:
                    l = i + 1
            if i == m:
                if nums2[j] >= nums1[i-1]:
                    if even:
                        if j == 0:
                            return float((nums1[i-1] + nums2[j]) / 2)
                        else:
                            return float((max(nums1[i-1], nums2[j-1]) + nums2[j]) / 2)
                    else:
                        return float(max(nums1[i-1], nums2[j-1]))
                else:
                    r = i - 1
            elif nums1[i] >= nums2[j-1] and nums2[j] >= nums1[i-1]:
                if even:
                    return float((max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2)
                else:
                    return float(max(nums1[i-1], nums2[j-1]))
            elif nums1[i] < nums2[j-1]:
                l = i + 1
            else:
                r = i - 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1.0,2.0], [3.0,4.0]))