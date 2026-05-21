# STROBOGRAMMATIC NUMBER

# Các cặp số khi xoay 180 độ
rotate = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

# ================= KIỂM TRA SỐ NGUYÊN TỐ =================
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# ================= KIỂM TRA STROBOGRAMMATIC =================
def isStrobogrammatic(n):
    s = str(n)

    left = 0
    right = len(s) - 1

    while left <= right:

        if s[left] not in rotate:
            return False

        if rotate[s[left]] != s[right]:
            return False

        left += 1
        right -= 1

    return True


# ================= XOAY SỐ 180 ĐỘ =================
def rotateNumber(n):
    s = str(n)

    result = ""

    for c in reversed(s):

        if c not in rotate:
            return -1

        result += rotate[c]

    return int(result)


# ================= a =================
print("a. So strobogrammatic < 1000000")

for i in range(1, 1000000):
    if isStrobogrammatic(i):
        print(i, end=" ")

# ================= b =================
print("\n\nb. So nguyen to strobogrammatic < 1000000")

for i in range(1, 1000000):
    if isStrobogrammatic(i) and isPrime(i):
        print(i, end=" ")

# ================= c =================
print("\n\nc. So strobogrammatic mo rong < 1000000")

for i in range(1, 1000000):

    rotated = rotateNumber(i)

    if rotated != -1:
        print(i, end=" ")

# ================= d =================
print("\n\nd. So nguyen to strobogrammatic mo rong < 1000000")

for i in range(1, 1000000):

    rotated = rotateNumber(i)

    if rotated != -1 and isPrime(i):
        print(i, end=" ")

# ================= e =================
print("\n\ne. Khong phai strobogrammatic, khong phai so nguyen to")
print("nhung xoay 180 do lai la so nguyen to")

for i in range(1, 1000000):

    rotated = rotateNumber(i)

    if rotated != -1:

        if (not isStrobogrammatic(i)
                and not isPrime(i)
                and isPrime(rotated)):

            print(i, end=" ")