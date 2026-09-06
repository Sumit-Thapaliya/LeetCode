class Solution(object):

    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            L = i + 1
            R = len(nums) - 1

            while L < R:

                sum = nums[i] + nums[L] + nums[R]

                # Check if current sum is closer
                if abs(sum - target) < abs(closest - target):
                    closest = sum

                if sum == target:
                    return sum

                elif sum < target:
                    L += 1

                else:
                    R -= 1

        return closest