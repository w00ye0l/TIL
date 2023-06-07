n = int(input())

mod = n % 8

if mod == 0:
    print(2)
elif mod <= 5:
    print(mod)
else:
    print(10 - mod)
