class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=[]
        for i in range(len(nums)):
            count=0
            max=nums[i]
            for j in range(len(nums)):
                if max>nums[j]:
                    count += 1
            a.append(count)
        return a
        
    # class Solution(object):
    # def smallerNumbersThanCurrent(self, nums):

    #     sorted_nums = sorted(nums)

    #     count = {}

    #     for i in range(len(sorted_nums)):
    #         if sorted_nums[i] not in count:
    #             count[sorted_nums[i]] = i

    #     answer = []

    #     for num in nums:
    #         answer.append(count[num])

    #     return answer