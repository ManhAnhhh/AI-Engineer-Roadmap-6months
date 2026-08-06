# ============================================================
# Day06 - exercises.py
# Bài tập: Hàm (Functions)
# ============================================================

# ------------------------------------------------------------
# Bài 1: Hàm tính giai thừa
# Viết hàm `tinh_giai_thua(n)` trả về giai thừa của n (n!).
# Nếu n < 0, trả về None. (Giai thừa của 0 là 1).
# ------------------------------------------------------------
# --- Viết code tại đây ---
n_test_1 = 5
n_test_2 = 0
n_test_3 = -2

def fac(n):
    if n < 0:
        return None
    else:
        result = 1
        for i in range(1,n + 1):
            print(i)
            result *= i
        return result
        
# ------------------------------------------------------------
# Bài 2: Phân tích danh sách số
# Viết hàm `phan_tich_so(numbers)` nhận vào một List các số.
# Hàm trả về 3 giá trị: số lớn nhất, số nhỏ nhất, và trung bình cộng.
# ------------------------------------------------------------
# --- Viết code tại đây ---
danh_sach = [12, 45, 2, 99, 34, 8, 77]

def phan_tich_so (numbers: list):
    so_lon_nhat = max(numbers)
    so_nho_nhat = min(numbers)
    tb = round(sum(numbers) / len(numbers), 2)
    
    return so_lon_nhat, so_nho_nhat, tb
    
print('Số lớn nhất, số nhỏ nhất, tb:', phan_tich_so(danh_sach))

# ------------------------------------------------------------
# Bài 3: Lọc từ dài (Sử dụng *args)
# Viết hàm `loc_tu_dai(min_length, *args)` nhận vào độ dài tối thiểu `min_length` 
# và một số lượng tùy ý các chuỗi.
# Trả về một List chứa các chuỗi có độ dài lớn hơn hoặc bằng `min_length`.
# ------------------------------------------------------------
# --- Viết code tại đây ---
min_len = 5
# test args: "AI", "Python", "Machine Learning", "Data", "Deep Learning", "Code"

def loc_tu_dai(min_length, *args):
    if min_length <= 0:
        return None
    else:
        return [x for x in args if len(x) >= min_length]
        
list_tu_dai = loc_tu_dai(min_len, "AI", "Python", "Machine Learning", "Data", "Deep Learning", "Code")
print(f'List từ dài: {list_tu_dai}')


# ------------------------------------------------------------
# Bài 4: Xử lý thông tin học viên (Sử dụng **kwargs)
# Viết hàm `tao_hoc_vien(ten, tuoi, **kwargs)` trả về một Dictionary chứa 
# thông tin học viên, bao gồm 'ten', 'tuoi' và tất cả các thông tin khác từ kwargs.
# ------------------------------------------------------------
# --- Viết code tại đây ---
ten_hv = "Nguyễn Thùy Linh"
tuoi_hv = 22
# test kwargs: khoa_hoc="AI Engineer", diem_tb=9.5
def tao_hoc_vien_ver1(ten, tuoi, **kwargs):
    print('Thông tin học viên')
    print(f'Tên: {ten}')
    print(f'Tuổi: {tuoi}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
def tao_hoc_vien_ver2(ten, tuoi, **kwargs):
    hoc_vien = {"name": ten, "tuoi": tuoi}
    hoc_vien.update(kwargs)
    
    return hoc_vien
        
tao_hoc_vien_ver1(ten_hv, tuoi_hv, khoa_hoc="AI Engineer", diem_tb=9.5)
tao_hoc_vien_ver2('Mạnh Anh', 23, khoa_hoc="Python", diem_tb=9.8)


# ------------------------------------------------------------
# Bài 5: Lambda và Filter/Map
# Cho danh sách các từ. Sử dụng lambda kết hợp với filter/map để:
# 1. Lọc ra các từ bắt đầu bằng chữ "A" hoặc "a".
# 2. Đổi tất cả các từ trong danh sách thành in hoa.
# ------------------------------------------------------------
# --- Viết code tại đây ---
words = ["Apple", "banana", "AI", "Agent", "python", "algorithm", "Data"]

list_start_a = list(filter(lambda x: x[0].lower() == 'a', words))
list_upper = list(map(lambda x: x.upper(), words))

print('Từ bắt đầu = "a" là các từ thuộc list:', list_start_a)
print('In hoa các từ thuộc list:', list_upper)