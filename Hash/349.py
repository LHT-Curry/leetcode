class Soluntion:
    def func1(self, s, t):
        num_set = set()
        res = set()
        for num in s:
            num_set.add(num)
        for num in t:
            if num in s:
                res.add(num)
        return list(res)

test = Soluntion()
res = test.func1([1,2,2,1], [2])
print(res)