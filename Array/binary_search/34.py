class Solution:
    def search_left(self, nums, target):
        left, right = 0, len(nums)-1
        res = -2
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                res = right
        return res
