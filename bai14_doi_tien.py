# Danh sách mệnh giá
money = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền
x = int(input("Nhap so tien X: "))

tong_to = 0

print(f"\nSo tien {x} duoc doi thanh:")

# Đổi tiền
for m in money:
    so_to = x // m
    x = x % m

    print(f"Loai {m} gom {so_to} to")

    tong_to += so_to

print("TONG CONG CO", tong_to, "TO")   