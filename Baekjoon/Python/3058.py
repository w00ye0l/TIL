for _ in range(int(input())):
    arr = list(map(int, input().split()))
    
    sum_, min_ = 0, float("inf")
    
    for i in range(7):
        if arr[i] % 2 == 0:
            sum_ += arr[i]
            min_ = min(min_, arr[i])
                                                            
    print(sum_, min_)