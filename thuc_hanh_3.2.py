from datetime import datetime, timedelta

#  i. THỜI GIAN HIỆN TẠI 
now = datetime.now()

print("===== THÔNG TIN HIỆN TẠI =====")
print("Năm hiện tại:", now.year)
print("Tháng hiện tại (chữ):", now.strftime("%B"))
print("Tuần thứ mấy trong năm:", now.strftime("%U"))
print("Tuần thứ mấy trong tháng:", (now.day - 1)//7 + 1)
print("Ngày thứ mấy trong năm:", now.strftime("%j"))
print("Ngày trong tháng:", now.day)
print("Thứ:", now.strftime("%A"))
print("Giờ phút giây:", now.strftime("%H:%M:%S"))

# ii. KHOẢNG CÁCH 2 NGÀY 
print("\n===== TÍNH KHOẢNG CÁCH 2 NGÀY =====")
d1 = input("Nhập ngày 1 (dd/mm/yyyy): ")
d2 = input("Nhập ngày 2 (dd/mm/yyyy): ")

date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")

diff = abs((date2 - date1).days)
print("Số ngày cách nhau:", diff)

#  iii. CHUYỂN CHUỖI SANG DATE 
print("\n===== CHUYỂN CHUỖI SANG DATE =====")
s = input("Nhập chuỗi (vd: Sep 18 2019 2:43PM): ")

date_obj = datetime.strptime(s, "%b %d %Y %I:%M%p")
print("Sau khi chuyển:", date_obj)

#  iv. CỘNG 5 GIÂY 
print("\n===== CỘNG 5 GIÂY =====")
new_time = now + timedelta(seconds=5)

print("Hiện tại:", now)
print("Sau khi cộng 5 giây:", new_time)