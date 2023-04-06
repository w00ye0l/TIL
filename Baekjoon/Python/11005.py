import string


def convert(n, b):
    # nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = string.digits + string.ascii_uppercase

    q, r = divmod(n, b)

    return convert(q, b) + nums[r] if q else nums[r]


n, b = map(int, input().split())

print(convert(n, b))
