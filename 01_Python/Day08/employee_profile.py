# ============================================================
# Day08 - employee_profile.py
# Mini Project: Quản lý nhân sự (Sử dụng Class)
# ============================================================

# Yêu cầu:
# Ở Day 07, một nhân viên được biểu diễn bằng 1 Dictionary:
# {"name": "Ngô Mạnh Anh", "age": 28, "department": "AI", "skills": ["Python"]}
#
# Hôm nay, chúng ta sẽ TÁI CẤU TRÚC (Refactor) bằng cách tạo một class `Employee`
# để đại diện cho một nhân viên. Việc này giúp code chuyên nghiệp và dễ mở rộng hơn.
#
# Yêu cầu:
# 1. Viết hàm `__init__(self, emp_id, name, age, department, skills)` 
# 2. Phương thức `hien_thi_thong_tin(self)`: In ra thông tin của nhân viên theo định dạng đẹp.
# 3. Phương thức `to_dict(self)`: Trả về một Dictionary chứa thông tin nhân viên (chức năng này
#    sẽ được dùng ở Day sau để lưu đối tượng (object) xuống file JSON).

# --- Viết code tại đây ---
class Employee:
    def __init__(self, emp_id, name, age, department, skills):
        self.emp_id = emp_id 
        self.name = name 
        self.age = age 
        self.department = department 
        self.skills = skills 
    def hien_thi_thong_tin(self):
        print("Thông tin nhân viên")
        print(f"{self.emp_id:<4} {self.name:<15} {self.age:<2} phòng ban {self.department} kỹ năng {",".join(self.skills)}")
    def to_dict(self):
        nhan_vien = {
           "emp_id": self.emp_id,
           "name": self.name,
           "age": self.age,
           "department": self.department,
           "skills": self.skills
        }
        return nhan_vien



# Kiểm thử (Hãy bỏ comment các dòng dưới đây sau khi viết xong code):
emp1 = Employee("E01", "Ngô Mạnh Anh", 28, "AI", ["Python", "Machine Learning"])
emp1.hien_thi_thong_tin()
print(emp1.to_dict())
