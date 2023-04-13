nums = [-1,0,1,2,-1,-4]
class Solution:
    def mergesort(self, nums):
        if len(nums) <=  1:
            return nums
        mid = len(nums)//2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res

    def NumSum(self, nums, target):
        nums = self.mergesort(nums)
        res = set()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[i] + nums[left] + nums[right] > target:
                    right -=1
                else:
                    left += 1
        res = list(res)
        res = [list(x) for x in res]
        return res


test = Solution()
print(test.NumSum([-1,0,1,2,-1,-4], 0))

