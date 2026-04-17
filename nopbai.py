dai = float(input("Nhập chiều dài hình khối chữ nhật (cm):>? "))
rong = float(input("Nhập chiều rộng hình khối chữ nhật (cm):>? "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm):>? "))
sole = int(input("Số lượng số lẻ cần hiển thị:>? "))

dien_tich_day = dai * rong
the_tich = dai * rong * cao

print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{sole}f}cm\u00b2")
print(f"Thể tích hình khối = {the_tich:.{sole}f}cm\u00b3")

print("Diện tích đáy hình chữ nhật = {0:.{1}f}cm\u00b2".format(dien_tich_day,sole))
print("Thể tích hình khối = {0:.{1}f}cm\u00b3".format(the_tich,sole))