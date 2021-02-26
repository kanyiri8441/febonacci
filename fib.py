def febonacci(s):
    x = 0
    y = 1
    if s==1:
        print(x)
    else:
        print(x)
        print(y)
        for i in range(2,s):
            z = x + y
            x = y
            y = z
            print(z)
print(febonacci(20))
