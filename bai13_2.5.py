import re

def chuan_hoa_chuoi(s):
    # 1. Xóa khoảng trắng đầu và cuối
    s = s.strip()
    
    # 2. Thay nhiều khoảng trắng thành 1
    s = re.sub(r'\s+', ' ', s)
    
    # 3. Xóa khoảng trắng trước dấu chấm, phẩy
    s = re.sub(r'\s+([.,])', r'\1', s)
    
    # 4. Đảm bảo sau dấu chấm/phẩy có 1 khoảng trắng (nếu chưa có)
    s = re.sub(r'([.,])([^\s])', r'\1 \2', s)

    return s


#  NHẬP CHUỖI 
print("Nhập chuỗi (có thể nhiều dòng, Enter dòng trống để kết thúc):")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

#XỬ LÝ TỪNG DÒNG
print("\n===== KẾT QUẢ =====")
for line in lines:
    print(chuan_hoa_chuoi(line))