a=1
b=1
fibNumberUpto = 10
count = 0
while(count<=fibNumberUpto):
    c = a+b
    a = b
    b = c
    print(c)
    count += 1