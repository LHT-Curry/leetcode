class Soluntion:
    def func1(self, s, t):
        char_dt = {}
        for i in s:
            if i in char_dt:
                char_dt[i] += 1
            else:
                char_dt[i] = 1
        for i in t:
            if i in char_dt:
                char_dt[i] -= 1
            else:
                return False
        for char in char_dt:
            if char_dt[char] != 0:
                return False
        return True
test = Soluntion()
res = test.func1("rat", "car")
print(res)