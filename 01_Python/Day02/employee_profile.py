# ============================================================
# Day02 - Mini Project: Hệ thống Xử lý Hồ sơ Nhân viên
# ============================================================

# MÔ TẢ: 
# Khách hàng gửi cho bạn một chuỗi dữ liệu thô chứa thông tin nhân viên 
# từ một form nhập liệu bị lỗi. Dữ liệu có chứa rất nhiều khoảng trắng thừa, 
# viết hoa/thường lộn xộn và không theo chuẩn.
# Định dạng chung: "   tên nhân viên | kỹ năng 1, kỹ năng 2 | lương cơ bản   "

raw_profile = "   nguYễn văN A | pyThon, machine learning, SQl | 25000000   "

# ============================================================
# YÊU CẦU THỰC HÀNH:
# ============================================================
# 1. Làm sạch khoảng trắng thừa ở hai đầu chuỗi (dùng strip).
# 2. Tách chuỗi đã làm sạch thành 3 phần: Tên, Kỹ năng, Lương (sử dụng split với dấu " | ").
# 3. Chuẩn hóa Tên: Viết hoa chữ cái đầu của mỗi từ (dùng hàm title()).
# 4. Chuẩn hóa Kỹ năng: Đưa tất cả về chữ HOA (upper) và thay dấu phẩy (,) thành dấu gạch ngang (-) bằng replace.
# 5. Ép kiểu Lương sang số nguyên (int).
# 6. Sử dụng F-string và Escape character (\n) để in ra Thẻ thông tin nhân viên thật đẹp.
#    - Lương phải có phân cách hàng nghìn bằng dấu phẩy (ví dụ: 25,000,000).
#    - Tên, Kỹ năng, Lương có thể dùng căn lề để các giá trị thẳng hàng nhau (ví dụ dùng {:<12}).

# ============================================================
# KẾT QUẢ MONG ĐỢI TRÊN MÀN HÌNH:
# ============================================================
# ========================================
# 💳 THẺ HỒ SƠ NHÂN VIÊN
# ========================================
# Tên:        Nguyễn Văn A
# Kỹ năng:    PYTHON - MACHINE LEARNING - SQL
# Mức lương:  25,000,000 VND
# ========================================

# ---------- VIẾT CODE CỦA BẠN DƯỚI ĐÂY ----------
clear_string = raw_profile.strip()
arr = clear_string.split(' | ')

# Lấy từng phần tử ra từ mảng arr
name = arr[0].title()
skills = arr[1].upper().replace(', ', ' - ')
salary = int(arr[2])

# Dùng f-string 3 nháy kép (f""") để in chuỗi trên nhiều dòng
card = f"""
========================================
[THẺ HỒ SƠ NHÂN VIÊN]
========================================
Tên:        {name}
Kỹ năng:    {skills}
Mức lương:  {salary:,.0f} VND
========================================
"""
print(card)
