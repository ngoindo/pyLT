def laSNT(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def demSNT(n):
    dem = 0
    for i in range(2, n):
        if laSNT(i):
            dem += 1
    return dem
def uocSNT(n):
    ds = []
    for i in range(1, n + 1):
        if n % i == 0 and laSNT(i):
            ds.append(i)
    return ds
n = int(input("Nhap n: "))
if laSNT(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai so nguyen to")
print("So luong SNT <", n, "la:", demSNT(n))
print("Cac uoc vua la uoc vua la SNT:")
print(uocSNT(n))
