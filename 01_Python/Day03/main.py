# ============================================================
# Day 03 - main.py  |  AI Engineer Roadmap
# Chủ đề: List trong Python
# Đây là "vở ghi chép" - nơi thực hành thử các khái niệm mới
# ============================================================

# -------------------------------------------------------
# 1. TẠO LIST
# -------------------------------------------------------
fruits = ["táo", "chuối", "cam", "xoài", "nho"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]   # List chứa nhiều kiểu dữ liệu
empty_list = []                     # List rỗng

print("=== TẠO LIST ===")
print(fruits)

# -------------------------------------------------------
# 2. TRUY CẬP PHẦN TỬ (INDEX)
# -------------------------------------------------------
print("\n=== INDEX ===")
print(fruits[0])    # táo    (đầu tiên)
print(fruits[2])    # cam    (thứ 3)
print(fruits[-1])   # nho    (cuối cùng)
print(fruits[-2])   # xoài  (áp cuối)

a = [1, 2]
b = [3, 4]
c = 'a123'

# ============================================================
# Day 03 - main.py  |  AI Engineer Roadmap
# Chủ đề: List trong Python
# Đây là "vở ghi chép" - nơi thực hành thử các khái niệm mới
# ============================================================

# -------------------------------------------------------
# 1. TẠO LIST
# -------------------------------------------------------
fruits = ["táo", "chuối", "cam", "xoài", "nho"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]   # List chứa nhiều kiểu dữ liệu
empty_list = []                     # List rỗng

print("=== TẠO LIST ===")
print(fruits)
print(type(fruits))                 # <class 'list'>

# -------------------------------------------------------
# 2. TRUY CẬP PHẦN TỬ (INDEX)
# -------------------------------------------------------
print("\n=== INDEX ===")
print(fruits[0])    # táo    (đầu tiên)
print(fruits[2])    # cam    (thứ 3)
print(fruits[-1])   # nho    (cuối cùng)
print(fruits[-2])   # xoài  (áp cuối)

# -------------------------------------------------------
# 3. SLICING
# -------------------------------------------------------
print("\n=== SLICING ===")
print(fruits[1:4])      # ['chuối', 'cam', 'xoài']
print(fruits[:3])       # ['táo', 'chuối', 'cam']
print(fruits[2:])       # ['cam', 'xoài', 'nho']
print(fruits[::2])      # ['táo', 'cam', 'nho']  (bước 2)
print(fruits[::-1])     # Đảo ngược list

# -------------------------------------------------------
# 4. THAY ĐỔI PHẦN TỬ
# -------------------------------------------------------
print("\n=== THAY ĐỔI PHẦN TỬ ===")
fruits[1] = "dưa hấu"
print(fruits)   # ['táo', 'dưa hấu', 'cam', 'xoài', 'nho']

# -------------------------------------------------------
# 5. CÁC PHƯƠNG THỨC QUAN TRỌNG
# -------------------------------------------------------
print("\n=== append() vs extend() ===")
list_a = [1, 2, 3]
list_b = [1, 2, 3]

list_a.append([4, 5])   # Thêm [4,5] như 1 phần tử DUY NHẤT
list_b.extend([4, 5])   # Thêm 4 và 5 như 2 phần tử RIÊNG LẺ

print("append([4,5]):", list_a)  # [1, 2, 3, [4, 5]]
print("extend([4,5]):", list_b)  # [1, 2, 3, 4, 5]

print("\n=== insert() ===")
veggies = ["cà rốt", "bắp cải", "khoai tây"]
veggies.insert(1, "súp lơ")    # Chèn vào vị trí index 1
print(veggies)

print("\n=== remove() và pop() ===")
colors = ["đỏ", "xanh", "vàng", "đỏ", "tím"]
colors.remove("đỏ")            # Xóa phần tử "đỏ" ĐẦU TIÊN tìm thấy
print("Sau remove:", colors)

removed = colors.pop()          # Xóa và trả về phần tử cuối
print("Phần tử bị xóa:", removed)
print("Sau pop():", colors)

removed_at = colors.pop(0)      # Xóa và trả về phần tử tại index 0
print("Phần tử bị xóa tại index 0:", removed_at)
print("Sau pop(0):", colors)

# -------------------------------------------------------
# 6. len(), in, count(), index()
# -------------------------------------------------------
print("\n=== len(), in, count(), index() ===")
scores = [85, 90, 75, 90, 60, 90, 55]
print("Số lượng:", len(scores))             # 7
print("90 có trong list?", 90 in scores)    # True
print("100 có trong list?", 100 in scores)  # False
print("90 xuất hiện:", scores.count(90), "lần")   # 3
print("Vị trí đầu tiên của 90:", scores.index(90))  # 1

# -------------------------------------------------------
# 7. sort() và reverse()
# -------------------------------------------------------
print("\n=== sort() và reverse() ===")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print("Trước khi sort:", nums)
nums.sort()
print("Sau sort() tăng dần:", nums)
nums.sort(reverse=True)
print("Sau sort() giảm dần:", nums)

nums2 = [3, 1, 4, 1, 5, 9]
print("\nsorted() (không thay đổi gốc):", sorted(nums2))
print("List gốc vẫn giữ nguyên:", nums2)

# -------------------------------------------------------
# 8. DUYỆT LIST BẰNG for
# -------------------------------------------------------
print("\n=== DUYỆT LIST ===")
animals = ["mèo", "chó", "thỏ", "hamster"]

# Cách 1: Duyệt từng phần tử
for animal in animals:
    print(f"  - {animal}")

# Cách 2: Duyệt kết hợp index với enumerate()
print()
for i, animal in enumerate(animals):
    print(f"  [{i}] {animal}")

# -------------------------------------------------------
# 9. LIST LỒNG NHAU (NESTED LIST)
# -------------------------------------------------------
print("\n=== NESTED LIST ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Ma trận 3x3:")
for row in matrix:
    print(" ", row)

print("Phần tử hàng 1, cột 2:", matrix[1][2])  # 6
