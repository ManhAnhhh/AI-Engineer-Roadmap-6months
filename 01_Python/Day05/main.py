# ============================================================
# Day 05 - main.py  |  AI Engineer Roadmap
# Chủ đề: Dictionary trong Python
# ============================================================

# ============================================================
# 1. TẠO DICTIONARY
# ============================================================
# Dictionary là tập hợp các cặp key-value.
# Key phải là kiểu dữ liệu Immutable (string, number, tuple).
# Value có thể là bất kỳ kiểu gì.

# Cách 1: Dùng dấu ngoặc nhọn {}
student = {
    "name": "Ngô Mạnh Anh",
    "age": 23,
    "city": "Hà Nội",
    "is_active": True
}

# Cách 2: Dùng hàm dict()
config = dict(model="GPT-4", temperature=0.7, max_tokens=1024)

print("=== Tạo Dictionary ===")
print(student)
print(config)


# ============================================================
# 2. TRUY CẬP GIÁ TRỊ
# ============================================================

print("\n=== Truy cập Dictionary ===")

# Cách 1: dict[key] — báo KeyError nếu key không tồn tại
print(student["name"])   # Ngô Mạnh Anh
print(student["age"])    # 23

# Cách 2: dict.get(key) — trả về None (hoặc giá trị mặc định) nếu key không tồn tại
print(student.get("city"))           # Hà Nội
print(student.get("score"))          # None
print(student.get("score", 0))       # 0  <-- Giá trị mặc định

# so sánh None dùng is None
print(student.get("city") is None)

# So sánh: dùng dict[key] khi chắc chắn key tồn tại,
#          dùng .get() khi không chắc (an toàn hơn)


# ============================================================
# 3. THÊM / SỬA DỮ LIỆU
# ============================================================

print("\n=== Thêm / Sửa ===")

# Thêm key mới
student["school"] = "Đại học Bách Khoa"
print("Sau khi thêm school:", student["school"])

# Sửa giá trị của key đã có
student["age"] = 24
print("Sau khi sửa age:", student["age"])

# update() — cập nhật nhiều key cùng lúc
student.update({"city": "TP. Hồ Chí Minh", "gpa": 3.8})
print("Sau khi update:", student)


# ============================================================
# 4. XÓA DỮ LIỆU
# ============================================================

print("\n=== Xóa dữ liệu ===")

# del dict[key] — xóa key, báo KeyError nếu không tồn tại
del student["is_active"]
print("Sau khi del is_active:", student)

# pop(key) — xóa key VÀ trả về giá trị của nó
removed_school = student.pop("school")
print("Đã xóa school:", removed_school)
print("Sau khi pop:", student)

# pop(key, default) — không báo lỗi nếu key không tồn tại
val = student.pop("non_existent_key", "Không có key này")
print("pop với key không có:", val)


# ============================================================
# 5. CÁC PHƯƠNG THỨC DUYỆT
# ============================================================

print("\n=== keys() / values() / items() ===")

# keys() — trả về tất cả các key
print("Keys:", list(student.keys()))

# values() — trả về tất cả các value
print("Values:", list(student.values()))

# items() — trả về các cặp (key, value) dưới dạng tuple
print("Items:", list(student.items()))


# ============================================================
# 6. KIỂM TRA KEY VỚI "in"
# ============================================================

print("\n=== Kiểm tra 'in' ===")

# 'in' kiểm tra trên KEY (không phải value)
print("name" in student)        # True
print("email" in student)       # False
print("not in:", "email" not in student)  # True


# ============================================================
# 7. DUYỆT DICTIONARY (Iteration)
# ============================================================

print("\n=== Duyệt Dictionary ===")

# Cách 1: Duyệt qua key
for key in student:
    print(f"  key: {key}")

# Cách 2: Duyệt qua key + value (phổ biến nhất)
for key, value in student.items():
    print(f"  {key}: {value}")

# Cách 3: Duyệt qua value
for value in student.values():
    print(f"  value: {value}")


# ============================================================
# 8. NESTED DICTIONARY (Dictionary lồng nhau)
# ============================================================

print("\n=== Nested Dictionary ===")

company = {
    "name": "AI Vietnam",
    "employees": {
        "E001": {"name": "Ngô Mạnh Anh", "role": "AI Engineer"},
        "E002": {"name": "Nguyễn Thùy Linh", "role": "Data Scientist"},
    }
}

# Truy cập nested
print(company["employees"]["E001"]["name"])    # Ngô Mạnh Anh
print(company["employees"]["E002"]["role"])    # Data Scientist

# Thêm nhân viên mới vào nested dict
company["employees"]["E003"] = {"name": "Trần Minh Quân", "role": "MLOps"}
print("Số nhân viên:", len(company["employees"]))


# ============================================================
# 9. DICTIONARY CHỨA LIST
# ============================================================

print("\n=== Dictionary chứa List ===")

ai_skills = {
    "python": ["list", "tuple", "set", "dict", "OOP"],
    "ml_frameworks": ["scikit-learn", "XGBoost", "LightGBM"],
    "dl_frameworks": ["TensorFlow", "PyTorch", "Keras"],
}

# Truy cập phần tử trong list bên trong dict
print(ai_skills["python"][0])          # list
print(ai_skills["dl_frameworks"][-1])  # Keras

# Thêm vào list bên trong dict
ai_skills["python"].append("comprehension")
print("Python skills:", ai_skills["python"])


# ============================================================
# 10. LIST CHỨA DICTIONARY
# ============================================================

print("\n=== List chứa Dictionary ===")

# Dạng này rất phổ biến khi làm việc với JSON / API / Database
users = [
    {"id": 1, "name": "Ngô Mạnh Anh", "score": 95},
    {"id": 2, "name": "Nguyễn Thùy Linh", "score": 88},
    {"id": 3, "name": "Trần Minh Quân", "score": 72},
]

# Duyệt và in thông tin
for user in users:
    print(f"  [{user['id']}] {user['name']} — Score: {user['score']}")

# Lọc user có score > 80
high_scorers = [u for u in users if u["score"] > 80]
print("High scorers:", [u["name"] for u in high_scorers])


# ============================================================
# 11. DICTIONARY COMPREHENSION
# ============================================================

print("\n=== Dictionary Comprehension ===")

# Cú pháp: {key_expr: value_expr for item in iterable [if condition]}

# Ví dụ 1: Tạo bảng bình phương
squares = {n: n**2 for n in range(1, 6)}
print("Bảng bình phương:", squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Ví dụ 2: Lọc từ dict có sẵn (chỉ lấy key có value > 80)
scores = {"An": 75, "Binh": 90, "Chi": 85, "Dung": 60}
passed = {name: score for name, score in scores.items() if score > 80}
print("Học sinh đạt:", passed)  # {'Binh': 90, 'Chi': 85}

# Ví dụ 3: Đảo ngược key-value
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print("Đảo ngược:", reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}

# Ví dụ 4: Chuẩn hóa (uppercase key)
raw_data = {"name": "ngô mạnh anh", "city": "hà nội"}
cleaned = {k: v.upper() for k, v in raw_data.items()}
print("Chuẩn hóa uppercase:", cleaned)


# ============================================================
# 12. XỬ LÝ JSON (rất quan trọng trong AI / API)
# ============================================================

print("\n=== Xử lý JSON ===")
import json

# json.dumps() — Chuyển Python dict → JSON string
python_dict = {
    "model": "gpt-4o",
    "messages": [
        {"role": "user", "content": "Xin chào!"},
        {"role": "assistant", "content": "Chào bạn, tôi có thể giúp gì?"}
    ],
    "temperature": 0.7,
    "stream": False
}

json_string = json.dumps(python_dict, ensure_ascii=False, indent=2)
print("JSON String:")
print(json_string)

# json.loads() — Chuyển JSON string → Python dict
api_response = '{"status": "success", "data": {"user_id": "U001", "tokens_used": 150}}'
parsed = json.loads(api_response)
print("\nParsed JSON:")
print(type(parsed))           # <class 'dict'>
print(parsed["data"]["user_id"])  # U001

# Đọc/ghi JSON file (phổ biến trong data science)
# json.dump(data, file)   — ghi ra file
# json.load(file)         — đọc từ file
