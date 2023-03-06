class Solution:
    def remove(self, nums, target):
        slow = fast = 0
        while fast <= len(nums) - 1:
            if nums[fast] == target:
                fast += 1
                continue
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        while slow <= len(nums) - 1:
            nums[slow] = 0
            slow += 1

test = Solution()
nums = [0,1,2,2,3,0,4,2]
test.remove(nums, 0)
print(nums)