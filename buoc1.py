# ===== NEN FILE =====

# Đọc file gốc
with open("fileName.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Tách từ
words = text.split()

# Danh sách từ duy nhất
unique_words = list(set(words))

# Mã hóa mỗi từ thành index
compressed = []

for w in words:
    compressed.append(str(unique_words.index(w)))

# Ghi file nén
with open("compressed.txt", "w", encoding="utf-8") as f:
    # dòng đầu lưu dictionary
    f.write("|".join(unique_words) + "\n")

    # dòng sau lưu index
    f.write(" ".join(compressed))

print("Da nen file thanh cong!")