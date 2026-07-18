# ============================================================
# Day 01 - exercises.py  |  AI Engineer Roadmap
# Chủ đề: Làm quen với Python
# ============================================================
# ============================================================
# Bài 1: Hello World & In ra màn hình
# ============================= ===============================
# Yêu cầu:
#   1. In ra dòng chữ: "Xin chào, tôi đang học Python!"
#   2. In ra tên của bạn và tuổi trên 2 dòng riêng biệt.
#   3. In ra kết quả của phép tính: 123 + 456 (không dùng máy tính, để Python tính).

# --- Viết code tại đây ---
print("Xin chào, tôi đang học Python!")
name = 'Mạnh Anh'
age = 23
print(name)
print(age)
print(123 + 456)
# ============================================================
# Bài 2: Biến & Kiểu dữ liệu
# ============================================================
# Yêu cầu:
#   1. Tạo các biến sau:
#       - ten       : chuỗi (str)   -> tên của bạn
#       - tuoi      : số nguyên (int)  -> tuổi của bạn
#       - chieu_cao : số thực (float)  -> chiều cao (mét), ví dụ: 1.72
#       - la_sv     : boolean          -> True nếu bạn là sinh viên
#   2. Dùng hàm type() để in ra kiểu dữ liệu của từng biến.
#   3. In ra thông tin theo định dạng:
#       "Xin chào, tôi là <ten>, <tuoi> tuổi, cao <chieu_cao>m."

# --- Viết code tại đây ---
ten = "Mạnh Anh"
tuoi = 23
chieu_cao = 1.72
la_sv = True

print(type(ten))
print(type(tuoi))
print(type(chieu_cao))
print(type(la_sv))

print(f"Xin chào, tôi là {ten}, {tuoi} tuổi, cao {chieu_cao}m.")

# ============================================================
# Bài 3: Toán tử & Biểu thức
# ============================================================
# Yêu cầu:
#   Cho 2 biến:  a = 17  ,  b = 5
#   Tính và in ra kết quả của:
#       1. Tổng, hiệu, tích, thương (a + b, a - b, a * b, a / b)
#       2. Thương nguyên (//), phần dư (%)
#       3. Lũy thừa: a ** b
#       4. Kiểm tra: a có chia hết cho b không? (in True hoặc False)

# --- Viết code tại đây ---
a = 17
b = 5
print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Thương:", a / b)
print("Thương nguyên:", a // b)
print("Phần dư:", a % b)
print("Lũy thừa:", a ** b)
print("a có chia hết cho b không?", a % b == 0)

# ============================================================
# Bài 4: Nhập liệu từ người dùng (input)
# ============================================================
# Yêu cầu:
#   1. Hỏi người dùng nhập vào tên và năm sinh.
#   2. Tính tuổi hiện tại (năm 2025 - năm sinh).
#   3. In ra: "Chào <tên>! Bạn <tuổi> tuổi."
#   Lưu ý: input() trả về string, cần chuyển đổi kiểu khi cần.

# --- Viết code tại đây ---
ten = input("Nhập vào tên của bạn: ")
tuoi = input("Nhập vào tuổi của bạn: ")
print(f"Chào {ten}! Bạn {int(tuoi)} tuổi.")

# ============================================================
# Bài 5: Chuỗi (String) nâng cao
# ============================================================
# Yêu cầu:
#   Cho biến: cau = "Python is awesome for AI"
#   1. In ra độ dài của chuỗi (dùng len()).
#   2. In ra chuỗi viết HOA toàn bộ.
#   3. In ra chuỗi viết thường toàn bộ.
#   4. Đếm chữ "a" (không phân biệt hoa thường) xuất hiện bao nhiêu lần.
#   5. Thay thế chữ "awesome" thành "great".
#   6. Kiểm tra chuỗi có bắt đầu bằng "Python" không? (in True/False)

# --- Viết code tại đây ---
cau = "Python is awesome for AI"
print("Độ dài chuỗi", len(cau))
print('Viết hoa', cau.upper())
print('Viết thường', cau.lower())
print('Số lần xuất hiện của "a"', cau.lower().count('a'))
print('Thay thế', cau.replace('awesome', 'great'))
print('Bắt đầu bằng "Python"', cau.startswith('Python'))

# ============================================================
# Bài 6: Tổng hợp - Tính chỉ số BMI
# ============================================================
# Yêu cầu:
#   1. Nhập vào cân nặng (kg) và chiều cao (mét) từ người dùng.
#   2. Tính BMI theo công thức: BMI = can_nang / (chieu_cao ** 2)
#   3. Làm tròn BMI đến 2 chữ số thập phân (dùng round()).
#   4. In ra kết quả theo định dạng:
#       "BMI của bạn là: <bmi>"
#   5. (Thử thách) In thêm phân loại:
#       BMI < 18.5  -> "Thiếu cân"
#       18.5 - 24.9 -> "Bình thường"
#       25.0 - 29.9 -> "Thừa cân"
#       >= 30       -> "Béo phì"

# --- Viết code tại đây ---
can_nang = float(input("Nhập vào cân nặng (kg): "))
chieu_cao = float(input("Nhập vào chiều cao (m): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"BMI của bạn là: {round(bmi, 2)}")

if bmi < 18.5:
    print("Phân loại: Thiếu cân")
elif 18.5 <= bmi < 25:
    print("Phân loại: Bình thường")
elif 25 <= bmi < 30:
    print("Phân loại: Thừa cân")
else:
    print("Phân loại: Béo phì")

    
# ============================================================
# Bài 7: Đổi phút → Giờ + Phút
# ============================================================
# Yêu cầu:
#   1. Nhập vào số phút bất kỳ từ người dùng (ví dụ: 135).
#   2. Tính số giờ và số phút còn lại.
#       Gợi ý: dùng toán tử // và %
#   3. In ra kết quả theo định dạng:
#       "135 phút = 2 giờ 15 phút"
#   4. (Thử thách) Xử lý thêm trường hợp:
#       - Nếu < 60 phút  -> chỉ in "X phút" (không in giờ)
#       - Nếu = 60 phút  -> in "1 giờ 0 phút"
#       - Nếu là số âm   -> in "Số phút không hợp lệ!"

# --- Viết code tại đây ---
phut = float(input("Nhập vào số phút: "))
if phut < 0:
    print("Số phút không hợp lệ!")
elif phut < 60:
    print(f"{int(phut)} phút")
else:
    gio = int(phut // 60)
    phut_con_lai = int(phut % 60)
    print(f"{int(phut)} phút = {gio} giờ {phut_con_lai} phút");


# Căn lề khi print
ten_1 = "Python"
ten_2 = "Java"
ten_3 = "JS"

# Thêm dấu gạch đứng | ở hai đầu để bạn dễ nhìn thấy ranh giới 15 ký tự nhé
print(f"Căn trái : |{ten_1:<15}|")
print(f"Căn phải : |{ten_2:>15}|")
print(f"Căn giữa : |{ten_3:^15}|")