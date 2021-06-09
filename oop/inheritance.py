from sys import setprofile


class BaseFunc:
    def __init__(self):
        self.a = 100
        self.b = 10
        self.c = 0

    def plus(self):
        return (self.a - self.c)

    def minus(self):
        return (self.a -self.b)
    def multipy(self):
        return (self.a * self.b)

    def get_default_max(self):
        return max(self.a, self.b, self.c)

    def get_default_min(self):
        return min(self.a, self.c, self.b)

    def range_max(self):
        for i in range(self.c, self.a, 10):
            print (i, end =" ")

class WorkFunc_c(BaseFunc):
    def __init__(self):
        # use BaseFunc's __init__ method, so will get the self.a , self.b, self.c value
        super().__init__()

# test
my_work_func_c = WorkFunc_c()
print (my_work_func_c.c)
print (my_work_func_c.b)
print (my_work_func_c.get_default_max())
print(my_work_func_c.get_default_min())
print(my_work_func_c.multipy())
print(my_work_func_c.plus())
print(my_work_func_c.minus())
print(my_work_func_c.range_max())
