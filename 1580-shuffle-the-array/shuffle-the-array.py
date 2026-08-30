class Solution(object):
    def shuffle(self, nums, n):
        b = []

        for i in range(n):
            b.append(nums[i])
            b.append(nums[i + n])

        return b

solution = Solution()

nums = [2, 5, 1, 3, 4, 7]
n = 3

print(solution.shuffle(nums, n))