class Solution:
    def NumSum(self, nums, target):
        dt = {}
        for i in range(len(nums)):
            if target-nums[i] in dt:
                return [dt[target-nums[i]], i]
            dt[nums[i]] = i


test = Solution()
print(test.NumSum([2,7,11,15], 18))