def reverse(x):
    if x < 0:
        x_rev = -int(str(abs(x))[::-1])
    else:
        x_rev = int(str(x)[::-1])

    if x_rev < -2**31 or x_rev > 2**31 - 1:
        return 0

    return x_rev

print(reverse(123))      # 321
print(reverse(-123))     # -321
print(reverse(1534236469))  # 0 (overflow)

"""
Exercise annotations:
- Name: Reverse Integer
- Runtime: 23ms
- Memory: 12.31MB
"""