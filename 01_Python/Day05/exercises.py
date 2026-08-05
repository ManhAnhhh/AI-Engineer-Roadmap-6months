# ============================================================
# Day 05 - exercises.py  |  AI Engineer Roadmap
# Chủ đề: Dictionary trong Python
# ============================================================

# ============================================================
# Bài 1: Tạo và truy cập Dictionary
# ============================================================
# Yêu cầu:
#   1. Tạo một dictionary `product` mô tả một sản phẩm AI, gồm các key:
#      "name", "price", "category", "in_stock" (True/False), "rating" (float).
#   2. In ra tên sản phẩm bằng dict[key].
#   3. Truy cập key "discount" (không tồn tại) bằng .get() với giá trị mặc định là 0.
#   4. In ra tất cả các key và tất cả các value của `product`.
#
# Gợi ý: Dùng .keys(), .values(), .get()

# --- Viết code tại đây ---
product = {
    "name": "Dell Vostro 5410",
    "price": 20000000,
    "category": "Laptop",
    "in_stock": True,
    "rating": 4.5
}

print(product["name"])
print(product.get("distcount", 0))

for key, value in product.items():
    print(f"  {key}: {value}") 


# ============================================================
# Bài 2: Thêm, sửa, xóa dữ liệu
# ============================================================
# Yêu cầu:
#   Cho dictionary sau:
#   employee = {"id": "E001", "name": "Ngô Mạnh Anh", "department": "AI", "salary": 15000000}
#
#   1. Thêm key "email" với giá trị "manh.anh@company.com".
#   2. Tăng "salary" thêm 20% (sửa giá trị bằng phép tính).
#   3. Dùng `pop()` để xóa "department" và in ra giá trị vừa bị xóa.
#   4. Dùng `update()` để cập nhật: "level": "Senior", "team": "Research".
#   5. In ra `employee` sau tất cả thao tác trên.
#
# Gợi ý: update(), pop(), dict[key] = value

# --- Viết code tại đây ---
employee = {"id": "E001", "name": "Ngô Mạnh Anh", "department": "AI", "salary": 15000000}
employee["email"] = "manh.anh@company.com"
employee["salary"] += employee["salary"] * 0.2

department = employee.pop("department")

print("removing department: ", department)

employee.update({"level": "Senior", "team": "Research"}) 
print(employee)


# ============================================================
# Bài 3: Duyệt Dictionary & Kiểm tra key
# ============================================================
# Yêu cầu:
#   Cho dictionary điểm số của học viên:
#   scores = {"Python": 92, "SQL": 78, "Machine Learning": 85, "Deep Learning": 70, "LangChain": 95}
#
#   1. Dùng vòng lặp `for key, value in ...items()` để in ra từng môn và điểm.
#   2. Kiểm tra xem môn "Docker" có trong dict không, in ra kết quả (True/False).
#   3. Tính điểm trung bình tất cả các môn.
#   4. Tìm môn có điểm CAO NHẤT (dùng max() với key=scores.get hoặc vòng lặp).
#
# Gợi ý: .items(), in, sum(), max()

# --- Viết code tại đây ---
scores = {"Python": 92, "SQL": 78, "Machine Learning": 85, "Deep Learning": 70, "LangChain": 95}

for key, value in scores.items():
    print(f'Môn: {key:<20} có điểm: {value:.2f}')
    
print("Docker" in scores)

diem_tb = sum(list(scores.values())) / len(list(scores.values()))
print("Điểm TB: ", diem_tb)

max_score = max(list(scores.values()))

score = [key for key, value in scores.items() if value == max_score]
print(f'Môn điểm cao nhất:', score[0])


# ============================================================
# Bài 4: Nested Dictionary
# ============================================================
# Yêu cầu:
#   Tạo dictionary `team` mô tả một team AI gồm 2 thành viên:
#   - "T001": name="Ngô Mạnh Anh", role="AI Engineer", skills=["Python", "PyTorch"]
#   - "T002": name="Nguyễn Thùy Linh", role="Data Scientist", skills=["Python", "SQL", "Pandas"]
#
#   1. In ra tên và role của từng thành viên bằng vòng lặp.
#   2. Thêm thành viên mới "T003": name="Trần Minh Quân", role="MLOps", skills=["Docker", "Kubernetes"]
#   3. Thêm skill "Git" vào danh sách skills của "T001".
#   4. In ra số lượng thành viên trong team.
#
# Gợi ý: team[id][key], .append(), len()

# --- Viết code tại đây ---
team = {
    "T001": {"name": "Ngô Mạnh Anh", "role": "AI Engineer", "skills": ["Python", "PyTorch"]},
    "T002": {"name": "Nguyễn Thùy Linh", "role": "Data Scientist", "skills": ["Python", "SQL", "Pandas"]},
}

for key, value in team.items():
    print(f"{value["name"]:<20} {value["role"]}")
    
team.update({"T003": {"name": "Trần Minh Quân", "role": "MLOps", "skills": ["Docker", "Kubernetes"]}})

team["T001"]["skills"].append("Git")

print("Số lượng thành viên:", len(team))

# ============================================================
# Bài 5: Dictionary Comprehension
# ============================================================
# Yêu cầu:
#   1. Dùng comprehension tạo dictionary `word_length` từ danh sách sau,
#      với key là từ và value là độ dài của từ đó:
#      words = ["python", "dictionary", "AI", "engineer", "roadmap"]
#
#   2. Cho dict: model_scores = {"BERT": 88.5, "GPT-2": 76.3, "T5": 91.2, "RoBERTa": 89.1}
#      Dùng comprehension tạo dict `top_models` chỉ chứa các model có score >= 88.
#
#   3. Đảo ngược dict sau (key → value, value → key):
#      status_code = {200: "OK", 404: "Not Found", 500: "Internal Server Error"}
#
# Gợi ý: {k: expr for k in list}, if condition

# --- Viết code tại đây ---
words = ["python", "dictionary", "AI", "engineer", "roadmap"]
model_scores = {"BERT": 88.5, "GPT-2": 76.3, "T5": 91.2, "RoBERTa": 89.1}
status_code = {200: "OK", 404: "Not Found", 500: "Internal Server Error"}

word_length = {word: len(word) for word in words}

print(word_length)

top_models = {key: value for key, value in model_scores.items() if value >= 88}
print(top_models)

print({value: key for key,value in status_code.items()})


# ============================================================
# Bài 6: Xử lý JSON
# ============================================================
# Yêu cầu:
#   1. Cho chuỗi JSON sau (giả lập response từ API AI):
#      Dùng json.loads() để parse thành Python dict.
#      In ra: model name, nội dung message đầu tiên, và total tokens.
#
#   2. Tạo một Python dict mô tả một request gửi lên API với:
#      - "model": "gemini-2.0-flash"
#      - "messages": list chứa 1 dict {"role": "user", "content": "Giải thích Dictionary là gì?"}
#      - "temperature": 0.5
#      Dùng json.dumps() để chuyển thành JSON string (có indent=2, ensure_ascii=False).
#      In ra kết quả.
#
# Gợi ý: import json, json.loads(), json.dumps()

# --- Viết code tại đây ---
import json

api_response_str = '''
{
  "model": "gemini-2.0-flash",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Dictionary là cấu trúc dữ liệu lưu trữ cặp key-value."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 50,
    "total_tokens": 70
  }
}
'''

dict_a = json.loads(api_response_str)

print(dict_a["model"])
print(dict_a["choices"][0]["message"])
print(dict_a["usage"]["total_tokens"])

json_disc_resquest = json.dumps(dict_a, ensure_ascii=False, indent=2)
