class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target<=nums[right]:
                left = mid + 1
            elif nums[left]<=target<nums[mid]:
                right = mid - 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
        return -1


test = Solution()
print(test.search([6,0,1,2, 4,5 ], 5))