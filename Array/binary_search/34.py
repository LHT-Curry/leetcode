class Solution:
    def search_left(self, nums, target):
        left, right = 0, len(nums)-1
        res = -2
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                res = right
        return res

    def search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        res = -2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                res = left
        return res

    def main(self, nums, target):
        left = self.search_left(nums, target)
        right = self.search_right(nums, target)
        if left == -2 or right == -2 or left+1>right-1:
            return [-1, -1]
        return [left+1, right-1]

test = Solution()
print(test.main([9,9,10], 9))
