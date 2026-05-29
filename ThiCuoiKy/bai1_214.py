dai = float(input("Nhap chieu dai: "))
rong = float(input("Nhap chieu rong: "))
cao = float(input("Nhap chieu cao: "))
sole = int(input("Nhap so luong so le can hien thi: "))

dien_tich_day = round(dai * rong, sole)
the_tich = round(dai * rong * cao, sole)

print("Dien tich day hinh chu nhat =", dien_tich_day, "cm\u00b2")
print("The tich hinh khoi =", the_tich, "cm\u00b3")
