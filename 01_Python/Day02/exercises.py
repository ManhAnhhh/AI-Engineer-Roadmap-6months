# ==========================================
# BÀI TẬP DAY 02 - XỬ LÝ CHUỖI (STRING)
# ==========================================

# Bài 1: Cơ bản về chuỗi
# Yêu cầu: 
# 1. Khai báo biến `my_name` chứa tên của bạn.
# 2. In ra độ dài tên của bạn (dùng hàm len).
# 3. In ra chữ cái đầu tiên và chữ cái cuối cùng trong tên của bạn (dùng index).
# 4. In ra tên của bạn nhưng viết hoa toàn bộ (dùng upper).

print("--- Bài 1 ---")
# Viết code của bạn ở đây
my_name = "ManhAnh"
print(len(my_name))
print(my_name[0])
print(my_name[-1])
print(my_name.upper())

# Bài 2: Slicing và Làm sạch dữ liệu (strip, lower)
# Cho chuỗi sau bị lỗi đánh máy (dư khoảng trắng và viết hoa lộn xộn):
raw_data = "   aI enGiNeeR roaDMap   "
# Yêu cầu:
# 1. Loại bỏ khoảng trắng thừa ở 2 đầu (dùng strip).
# 2. Đưa toàn bộ về chữ thường (dùng lower).
# 3. Dùng Slicing để lấy ra chữ "engineer" từ chuỗi đã làm sạch và in ra màn hình.

print("\n--- Bài 2 ---")
# Viết code của bạn ở đây
print(raw_data.strip())
print(raw_data.strip().lower())
clean_data = raw_data.strip().lower()
print(clean_data.split()[1])

# Bài 3: Replace, Split và Join
# Cho đoạn văn bản chứa danh sách kỹ năng ngăn cách bằng dấu phẩy:
skills_str = "Python, SQL, Machine Learning, Deep Learning"
# Yêu cầu:
# 1. Dùng split để chuyển chuỗi này thành 1 mảng (list) các kỹ năng.
# 2. Dùng join để ghép mảng đó lại thành 1 chuỗi, nhưng ngăn cách nhau bởi dấu gạch ngang " - ".
# 3. Thay thế (replace) chữ "Deep Learning" thành "AI" trong chuỗi gốc ban đầu.

print("\n--- Bài 3 ---")
# Viết code của bạn ở đây
skills_arr = skills_str.split(', ')
print(skills_arr)
print(' - '.join(skills_arr))
print(skills_str.replace('Deep Learning', 'AI'))

# Bài 4: Kiểm tra chuỗi con (in) và Escape characters
# Cho đoạn văn bản:
paragraph = "Hôm nay tôi học Python. Ngôn ngữ này rất thú vị."
# Yêu cầu:
# 1. Kiểm tra xem chữ "Python" có nằm trong đoạn văn hay không (dùng toán tử in) và in ra kết quả (True/False).
# 2. In ra đoạn văn trên thành 2 dòng, dòng 1 là câu đầu, dòng 2 là câu sau. Sử dụng Escape character (\n). (Lưu ý có khoảng trắng dư cần xử lý hoặc dùng cách nào đó để in cho đẹp).

print("\n--- Bài 4 ---")
# Viết code của bạn ở đây
if 'Python' in paragraph:
    print('true')
else:
    print('false')


# Bài 5: Xử lý input từ người dùng và F-string nâng cao
# Yêu cầu:
# 1. Dùng hàm input() để yêu cầu người dùng nhập vào tuổi của họ.
# 2. Chuyển đổi dữ liệu nhập vào thành số nguyên (int).
# 3. Tính năm sinh của người đó (giả sử năm hiện tại là 2024).
# 4. Dùng F-string để in ra câu: "Bạn sinh năm [năm sinh]. Năm nay bạn [tuổi] tuổi."
#    Trong đó, độ tuổi phải được canh lề phải chiếm 5 khoảng trống (ví dụ: {age:>5}).

print("\n--- Bài 5 ---")
# Viết code của bạn ở đây

age = int(input('Nhập tuổi: '))
years = 2024 - age
print(f'Năm sinh: {years}')
print(f'Bạn sinh năm {years}. Năm nay bạn {age:>5} tuổi.')