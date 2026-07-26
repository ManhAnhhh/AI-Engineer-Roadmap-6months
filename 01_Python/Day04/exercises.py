# ============================================================
# Day 04 - exercises.py  |  AI Engineer Roadmap
# Chủ đề: Tuple và Set trong Python
# ============================================================

# ============================================================
# Bài 1: Thao tác với Tuple & Unpacking
# ============================================================
# Yêu cầu:
#   1. Tạo một tuple `user_info` chứa: ("Ngô Mạnh Anh", 22, "Hà Nội", "AI Engineer").
#   2. In ra màn hình phần tử đầu tiên và phần tử cuối cùng của tuple.
#   3. Dùng tuple unpacking để gán các giá trị trên vào 4 biến: `name`, `age`, `city`, `job`.
#   4. In ra câu giới thiệu: "Tôi tên là [name], [age] tuổi, sống tại [city] và làm nghề [job]."

# --- Viết code tại đây ---
user_info = ("Ngô Mạnh Anh", 23, "Hà Nội", "AI Engineer")
print(user_info[0])
print(user_info[-1])
name, age, city, job = user_info
print(f"Tôi tên là {name}, {age} tuổi, sống tại {city} và làm nghề {job}.")

# ============================================================
# Bài 2: Immutable & Chuyển đổi kiểu dữ liệu
# ============================================================
# Yêu cầu:
#   Cho tuple: `coordinates = (21.0285, 105.8542)` (Tọa độ Hà Nội)
#   1. Thử thay đổi phần tử đầu tiên thành `20.0000` và quan sát lỗi (comment lại dòng lỗi).
#   2. Làm cách nào để thay đổi tọa độ trên? (Gợi ý: Chuyển tuple -> list -> sửa -> chuyển lại tuple).
#   3. In ra `coordinates` mới sau khi đã sửa.

# --- Viết code tại đây ---
coordinates = (21.0285, 105.8542)
# coordinates[0] = 'a'
# 'tuple' object does not support item assignment
list_coor = []
list_coor.extend(coordinates)
list_coor[0] = 20.0000
coordinates = tuple(list_coor)
print(coordinates)
# có thể dùng ngắn hơn
# list_coor = list(coordinates) # k cần p dùng extend

# ============================================================
# Bài 3: Loại bỏ phần tử trùng lặp với Set
# ============================================================
# Yêu cầu:
#   Cho danh sách email đăng ký sự kiện bị trùng lặp:
#   `emails = ["an@gmail.com", "binh@yahoo.com", "an@gmail.com", "chi@gmail.com", "binh@yahoo.com", "dung@hotmail.com"]`
#   1. Chuyển `emails` thành Set để loại bỏ các email trùng lặp.
#   2. In ra số lượng email duy nhất đã đăng ký.
#   3. Chuyển kết quả lại thành List và sắp xếp theo thứ tự bảng chữ cái (Alphabet A -> Z).

# --- Viết code tại đây ---
emails = ["an@gmail.com", "binh@yahoo.com", "an@gmail.com", "chi@gmail.com", "binh@yahoo.com", "dung@hotmail.com"]
unique_emails = set(emails)
print('Số lượng emails', len(unique_emails))    
# Trường hợp mà muốn tìm ra email đăng ký 1 lần (bỏ qua những email đăng ký nhiều lần) -> dùng distionary (dist)
bang_dem_thu_cong = {}
for email in emails:
    if email in bang_dem_thu_cong:
        bang_dem_thu_cong[email] += 1
    else:
        bang_dem_thu_cong[email] = 1
# sorted() nhận tất cả các kiểu dữ liệu lặp được (Iterable), bao gồm Tuple, List, Set, Dictionary, String,..
# hàm sorted() sẽ LUÔN LUÔN trả về kết quả là một List mới đã được sắp xếp.
emails_sorterd = sorted(unique_emails, reverse = False)
print(emails_sorterd)

# ============================================================
# Bài 4: Phép toán Tập hợp (Set Operations)
# ============================================================
# Yêu cầu:
#   Cho danh sách kỹ năng của 2 ứng viên:
#   `candidate_A = {"Python", "SQL", "Git", "Docker", "PyTorch"}`
#   `candidate_B = {"Python", "Java", "Git", "Kubernetes", "TensorFlow"}`
#   1. Tìm tất cả các kỹ năng mà ít nhất 1 trong 2 ứng viên có (Union).
#   2. Tìm các kỹ năng mà CẢ HAI ứng viên đều có (Intersection).
#   3. Tìm các kỹ năng mà ứng viên A có nhưng ứng viên B KHÔNG có (Difference).

# --- Viết code tại đây ---
candidate_A = {"Python", "SQL", "Git", "Docker", "PyTorch"}
candidate_B = {"Python", "Java", "Git", "Kubernetes", "TensorFlow"}
union_a_b = candidate_A.union(candidate_B)
intersection_a_b = candidate_A.intersection(candidate_B) 
diff_candicate = candidate_A.difference(candidate_B) 

# ============================================================
# Bài 5: Quản lý danh mục sản phẩm (Add, Remove, Discard)
# ============================================================
# Yêu cầu:
#   Bắt đầu với tập hợp các tags bài viết: `tags = {"AI", "Python", "Machine Learning"}`
#   1. Thêm tag `"Deep Learning"` vào tập hợp.
#   2. Thử thêm lại tag `"Python"` và kiểm tra kích thước tập hợp xem có tăng không.
#   3. Dùng `discard()` để xóa tag `"Java"` (không tồn tại trong set).
#   4. Dùng `remove()` để xóa tag `"AI"`.
#   5. In ra kết quả tập hợp `tags` cuối cùng.

# --- Viết code tại đây ---
tags = {"AI", "Python", "Machine Learning"}
tags.add('Python')
print(len(tags)) # phần tử trùng -> len giữ nguyên
tags.discard('Java')
print(tags)

