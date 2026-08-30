class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()

        n = len(num)

        if n % 2 == 1:
            return num[n // 2]
        else:
            return (num[n // 2 - 1] + num[n // 2]) / 2.0
num1=[1,2]
num2=[3,4]
a=Solution()
b=a.findMedianSortedArrays(num1,num2)
print(b)