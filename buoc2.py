# ===== GIAI NEN FILE =====

with open("compressed.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Lấy dictionary
dictionary = lines[0].strip().split("|")

# Lấy danh sách index
indexes = lines[1].strip().split()

# Khôi phục văn bản
result = []

for i in indexes:
    result.append(dictionary[int(i)])

original_text = " ".join(result)

print("\nVan ban khoi phuc:")
print(original_text)