t = int(input())

for _ in range(t):
    arr = input().replace(" ", "")
    modi = list(arr.split('='))

    if eval(modi[0]) == int(modi[1]):
        print("correct")
    else:
        print("wrong answer")
