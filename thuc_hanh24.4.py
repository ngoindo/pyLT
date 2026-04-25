import math

# a
a = lambda n: abs(n)

# b
b = lambda n: n + 15

# c
c = lambda x, y: x * y

# d
d = lambda n: n % 13 == 0 or n % 19 == 0

# e
e = lambda r: math.pi * r * r

# f
f = lambda d, r: 2 * (d + r)

# g
g = lambda n: int(math.isqrt(n))**2 == n

# h
h = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i
i = lambda a, b, c: (
    "không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else (
        "tam giác đều"
        if a == b == c
        else (
            "tam giác vuông"
            if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
            else (
                "tam giác cân"
                if a == b or b == c or a == c
                else "tam giác thường"
            )
        )
    )
)