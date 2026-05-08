from collections import Counter

# Nhập 2 chuỗi
S1 = input("Nhap S1: ")
S2 = input("Nhap S2: ")

# Đưa vào Counter
dict1 = Counter(S1)
dict2 = Counter(S2)

print("\na) Ky tu xuat hien trong ca 2 chuoi:")

common = dict1 & dict2

for k in common:
    print(k, end=" ")

print("\n\nb) So ky tu khac nhau:")

s1_not_s2 = 0
s2_not_s1 = 0

for k in dict1:
    if k not in dict2:
        s1_not_s2 += 1

for k in dict2:
    if k not in dict1:
        s2_not_s1 += 1

print("So ky tu co trong S1 nhung khong co trong S2:", s1_not_s2)
print("So ky tu co trong S2 nhung khong co trong S1:", s2_not_s1)

print("\nc) Ky tu khac nhau:")

print("Co trong S1 nhung khong co trong S2:")
for k in dict1:
    if k not in dict2:
        print(k, end=" ")

print("\nCo trong S2 nhung khong co trong S1:")
for k in dict2:
    if k not in dict1:
        print(k, end=" ")