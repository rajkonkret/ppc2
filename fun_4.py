def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest funkcja fun2")

    return fun2  # return a+b


xFun1 = fun1()  # xfun1 ? => zwrociło fun2
print(type(xFun1))
xFun1()   # wywołanie fun2

