scp = lambda n: int(n ** 0.5) ** 2 == n
sht = lambda n: sum(i for i in range(1, n) if n % i == 0) == n
print("So chinh phuong tu 1 -> 10000:")
for i in range(1, 10001):
    if scp(i):
        print(i, end=" ")
print("\n")
print("So hoan thien tu 1 -> 10000:")
for i in range(1, 10001):
    if sht(i):
        print(i, end=" ")
