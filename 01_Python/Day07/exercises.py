# ============================================================
# Day07 - exercises.py
# Bài tập: Xử lý File và Ngoại lệ
# ============================================================

# ------------------------------------------------------------
# Bài 1: Ép kiểu an toàn (Try/Except)
# Viết hàm `chuyen_thanh_so_nguyen(chuoi)` nhận vào một chuỗi.
# Cố gắng ép kiểu chuỗi đó sang số nguyên (int).
# Nếu thành công, trả về số nguyên đó.
# Nếu thất bại (ValueError), in ra thông báo lỗi và trả về None.
# ------------------------------------------------------------
# --- Viết code tại đây ---
test_1 = "123"
test_2 = "3.14"
test_3 = "hello"

def chuyen_thanh_so_nguyen(s: str):
    try:
        so_nguyen = int(s)
    except Exception as e:
       print("Lỗi chuyển đổi, lỗi cụ thể", e)
       return None
    else:
        return so_nguyen
print(chuyen_thanh_so_nguyen(test_1))
print(chuyen_thanh_so_nguyen(test_2))
print(chuyen_thanh_so_nguyen(test_3))

# ------------------------------------------------------------
# Bài 2: Đọc file an toàn
# Viết hàm `doc_noi_dung_file(file_path)` nhận vào đường dẫn file.
# Sử dụng Try/Except để mở và đọc toàn bộ nội dung file (string).
# Bắt lỗi `FileNotFoundError` nếu file không tồn tại và trả về thông báo lỗi.
# Nếu đọc thành công, trả về nội dung file.
# ------------------------------------------------------------
# --- Viết code tại đây ---
file_khong_ton_tai = "khong_co_thuc.txt"

def doc_noi_dung_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            noi_dung = f.read()
    except FileNotFoundError:
        print("File", file_path, "không tồn tại")
    else:
        return noi_dung

ket_qua_1 = doc_noi_dung_file(file_khong_ton_tai)
print(ket_qua_1)
        
# ------------------------------------------------------------
# Bài 3: Lọc dữ liệu lỗi từ danh sách
# Cho một danh sách hỗn hợp gồm số và chuỗi.
# Sử dụng vòng lặp và Try/Except để tính TỔNG của tất cả các SỐ (cả int và float) trong danh sách.
# Cố gắng ép kiểu từng phần tử sang float, nếu sinh lỗi ValueError thì bỏ qua phần tử đó.
# ------------------------------------------------------------
# --- Viết code tại đây ---
mixed_data = [10, "20", "abc", 30.5, "40.5", "Python", 5]

def convert_list_to_float(l:list):
    tong = 0
    for ele in l:
        try:
            tong += float(ele)
        except ValueError:
            continue
    return tong
    
print(convert_list_to_float(mixed_data))



