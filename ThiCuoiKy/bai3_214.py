scp = lambda n: int(n ** 0.5) ** 2 == n
n = int(input("Nhap n: "))
if scp(n):
    print(n, "la so chinh phuong")
else:
    print(n, "khong phai so chinh phuong")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
tamgiac = lambda a, b, c: a + b > c and a + c > b and b + c > a
if tamgiac(a, b, c):
    if a == b == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        print("Tam giac can")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")
