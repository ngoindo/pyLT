# ================= BÀI 6 =================
print("===== BÀI 6: ĐẾM SỐ LẦN XUẤT HIỆN =====")
S = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

# Tách từ (đơn giản)
words = S.lower().split()
count = words.count(word.lower())

print(f"Số lần xuất hiện của '{word}' là:", count)


# ================= BÀI 7 =================
print("\n===== BÀI 7: THAY 'not...poor' =====")
S = input("Nhập chuỗi S: ")

# Tìm vị trí
pos_not = S.find("not")
pos_poor = S.find("poor")

# Kiểm tra điều kiện
if pos_not != -1 and pos_poor != -1 and pos_not < pos_poor:
    S = S[:pos_not] + "good" + S[pos_poor + 4:]

print("Kết quả:", S)