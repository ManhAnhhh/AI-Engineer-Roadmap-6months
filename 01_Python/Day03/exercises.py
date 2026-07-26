# ============================================================
# Day 03 - exercises.py  |  AI Engineer Roadmap
# Chủ đề: List trong Python
# ============================================================

# ============================================================
# Bài 1: Tạo và truy cập List
# ============================================================
# Yêu cầu:
#   1. Tạo list tên: my_list chứa 5 môn học của bạn (chuỗi).
#   2. In ra:
#       - Môn học đầu tiên (dùng index dương).
#       - Môn học cuối cùng (dùng index âm).
#       - Số lượng môn học (dùng len()).
#   3. Kiểm tra xem "Toán" có trong danh sách không, in True/False.

# --- Viết code tại đây ---
my_list = ['Toán', 'Văn', 'Anh', 'Thể Dục', 'Lịch Sử']
print(my_list[0])
print(my_list[-1])
print(len(my_list))
print('Toán' in my_list)

# ============================================================
# Bài 2: Slicing List
# ============================================================
# Yêu cầu:
#   Cho list: diem_so = [5, 7, 8, 6, 9, 4, 10, 3, 7, 8]
#   1. In ra 3 phần tử đầu tiên.
#   2. In ra 3 phần tử cuối cùng.
#   3. In ra các phần tử từ index 2 đến index 6 (bao gồm cả 6).
#   4. In ra list đảo ngược (dùng slicing, không dùng reverse()).
#   5. In ra các phần tử tại vị trí chẵn (index 0, 2, 4, ...).

# --- Viết code tại đây ---
diem_so = [5, 7, 8, 6, 9, 4, 10, 3, 7, 8]
print(diem_so[:3])       # Câu 1: 3 phần tử đầu
print(diem_so[-3:])      # Câu 2: 3 phần tử cuối
print(diem_so[2:7])      # Câu 3: index 2 → 6
print(diem_so[::-1])     # Câu 4: đảo ngược bằng slicing
print(diem_so[::2])      # Câu 5: vị trí chẵn (index 0, 2, 4, ...)

# ============================================================
# Bài 3: Thêm và xóa phần tử
# ============================================================
# Yêu cầu:
#   Bắt đầu với list: gio_hang = ["áo", "quần", "giày"]
 
#   1. Dùng append() thêm "mũ" vào cuối.
#   2. Dùng insert() thêm "tất" vào vị trí index 1.
#   3. Dùng extend() thêm thêm ["dép", "túi xách"] vào cuối.
#   4. In ra list sau mỗi thao tác.
#   5. Dùng remove() xóa "quần" khỏi list.
#   6. Dùng pop() lấy ra phần tử cuối và in ra phần tử đó.
#   7. In ra list sau cùng.

# --- Viết code tại đây ---
gio_hang = ["áo", "quần", "giày"]
gio_hang.append('mũ')              # Câu 1: thêm vào cuối
print(gio_hang)
gio_hang.insert(1, 'tất')          # Câu 2: chèn vào index 1
print(gio_hang)
gio_hang.extend(['dép', 'túi xách'])  # Câu 3: nối nhiều phần tử
print(gio_hang)
gio_hang.remove('quần')            # Câu 5: xóa 'quần'
last_gio_hang = gio_hang.pop()     # Câu 6: xóa và lấy phần tử cuối
print('Phần tử bị pop():', last_gio_hang)
print(gio_hang)                    # Câu 7: list sau cùng

# ============================================================
# Bài 4: Tìm kiếm và thống kê
# ============================================================
# Yêu cầu:
#   Cho list điểm thi: ket_qua = [8, 5, 9, 7, 5, 10, 5, 6, 9, 8]
#   1. Tìm điểm cao nhất (dùng max()).
#   2. Tìm điểm thấp nhất (dùng min()).
#   3. Tính tổng điểm (dùng sum()).
#   4. Tính điểm trung bình (làm tròn 2 chữ số).
#   5. Đếm xem điểm 5 xuất hiện bao nhiêu lần.
#   6. Tìm vị trí đầu tiên của điểm 9.

# --- Viết code tại đây ---
ket_qua = [8, 5, 9, 7, 5, 10, 5, 6, 9, 8]
max_kq = max(ket_qua)
min_kq = min(ket_qua)
sum_kq = sum(ket_qua)
avg_kq = round(sum_kq / len(ket_qua), 2)
count_5 = ket_qua.count(5)
index_9 = ket_qua.index(9)
print(f'Điểm cao nhất  : {max_kq}')
print(f'Điểm thấp nhất : {min_kq}')
print(f'Tổng điểm      : {sum_kq}')
print(f'Điểm trung bình: {avg_kq}')
print(f'Điểm 5 xuất hiện: {count_5} lần')
print(f'Vị trí đầu tiên của điểm 9: index {index_9}')

# ============================================================
# Bài 5: Sắp xếp List
# ============================================================
# Yêu cầu:
#   Cho list: nhiet_do = [32, 18, 25, 12, 37, 20, 28]
#   1. Tạo một list mới là bản sao đã sắp xếp tăng dần
#      (dùng sorted(), giữ nguyên list gốc).
#   2. Sắp xếp list gốc theo thứ tự giảm dần (dùng sort(reverse=True)).
#   3. In ra list gốc và list đã được sorted() để thấy sự khác biệt.

# --- Viết code tại đây ---
nhiet_do = [32, 18, 25, 12, 37, 20, 28]

sort_nhiet_do = sorted(nhiet_do)
nhiet_do.sort(reverse = True)
print(nhiet_do)
print(sort_nhiet_do)
# ============================================================
# Bài 6: Duyệt List
# ============================================================
# Yêu cầu:
#   Cho list: san_pham = ["Laptop", "Chuột", "Bàn phím", "Màn hình", "Tai nghe"]
#   1. Dùng vòng lặp for để in ra từng sản phẩm theo định dạng:
#          "1. Laptop"
#          "2. Chuột"
#          ...
#      (dùng enumerate() với start=1)
#   2. Tạo một list mới tên gia_tri chứa độ dài tên của từng sản phẩm.
#      (dùng for loop và append())
#   3. In ra gia_tri.

# --- Viết code tại đây ---
san_pham = ["Laptop", "Chuột", "Bàn phím", "Màn hình", "Tai nghe"]

#for i in range(len(san_pham)):
#   print(f'{i + 1}. {san_pham[i]}')

gia_tri = []
for j, sp in enumerate(san_pham, 1):
    print(f'{j}. {sp}')
    gia_tri.append(len(sp))
print(gia_tri)    

# ============================================================
# Bài 7: List lồng nhau (Nested List) - Thử thách
# ============================================================
# Yêu cầu:
#   Cho bảng điểm lớp học (dạng nested list):
#   bang_diem = [
#       ["An",   8, 7, 9],
#       ["Bình", 6, 8, 7],
#       ["Chi",  9, 10, 8],
#       ["Dũng", 5, 6, 7],
#   ]
#   Mỗi hàng: [Tên, Điểm Toán, Điểm Lý, Điểm Hóa]
#
#   1. In ra tên và điểm của tất cả học sinh theo định dạng:
#          "An   | Toán: 8 | Lý: 7 | Hóa: 9"
#   2. Tính và in ra điểm trung bình của từng học sinh.
#   3. Tìm và in ra tên học sinh có điểm trung bình cao nhất.

# --- Viết code tại đây ---
bang_diem = [
   ["An",   8, 7, 9],
   ["Bình", 6, 8, 7],
   ["Chi",  9, 10, 8],
   ["Dũng", 5, 6, 7],
]
diem_max = 0
for i, ele in enumerate(bang_diem):
    print(f'{bang_diem[i][0]:<5} Toán: {bang_diem[i][1]} | Lý: {bang_diem[i][2]:<2} | Hóa: {bang_diem[i][3]}')
    diem = bang_diem[i][1:]
    diem_tb = round(sum(diem) / len(diem), 2)
    print(f'Điểm trung bình: {diem_tb}')
    
    if diem_max < diem_tb:
        diem_max = diem_tb
        ng_max = bang_diem[i][0]
        
print('Học sinh có điểm trung bình cao nhất:', ng_max)