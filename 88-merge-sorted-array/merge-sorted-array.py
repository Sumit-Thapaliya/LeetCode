# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         a=[]
#         b=[]
#         for i in range(m):
#             a.append(nums1[i])
#         for i in range(n):
#             b.append(nums2[i])
#         a.extend(b)
#         a.sort()
#         for i in range(m + n):
#             nums1[i] = a[i]

#         return nums1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        return nums1
        