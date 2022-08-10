angular = []

for _ in range(3):
    angular.append(int(input()))

sum_ = sum(angular)
set_ = set(angular)

if sum_ == 180:
    if len(set_) == 1:
        print('Equilateral')
    elif len(set_) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
