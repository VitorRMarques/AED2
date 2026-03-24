def func_A(n):
    c = 0
    for i in range(1, n):
        c += 1
        print("--------")
        print(i)
    for j in range(1, n):
        c += 2
        print("--------")
        print(j)
    return c
print("------------")
print(func_A(31))