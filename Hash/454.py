class Solution:
    def NumSum(self, A, B, C, D, target):
        dt = {}
        res = 0
        for i in A:
            for j in B:
                s = i + j
                if s in dt:
                    dt[s] += 1
                else:
                    dt[s] = 1
        for i in C:
            for j in D:
                s = i + j
                if target-s in dt:
                    res += dt[target-s]
        return res


test = Solution()
print(test.NumSum([1, 2], [-2, -1], [-1, 2], [0, 2], 0))