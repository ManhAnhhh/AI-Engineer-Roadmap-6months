# ============================================================
# Day06 - employee_profile.py
# Mini Project: Quản lý nhân sự (Module hóa bằng hàm)
# ============================================================

# Yêu cầu:
# Viết các hàm để quản lý danh sách nhân viên (sử dụng Dictionary chứa Dictionary).
#
# 1. Hàm them_nhan_vien(db, emp_id, name, age, department, skills)
#    - Thêm một nhân viên mới vào db. Nếu emp_id đã tồn tại, in ra thông báo lỗi.
#
# 2. Hàm tim_nhan_vien_theo_id(db, emp_id)
#    - Trả về dictionary thông tin của nhân viên nếu tìm thấy, ngược lại trả về None.
#
# 3. Hàm liet_ke_theo_phong_ban(db, department)
#    - Trả về danh sách (List) các nhân viên thuộc phòng ban `department`.
#
# 4. Hàm xoa_nhan_vien(db, emp_id)
#    - Xóa nhân viên khỏi db dựa trên emp_id và trả về True. Nếu không có, trả về False.

# --- Viết code tại đây ---
# Khởi tạo database trống
employee_db = {}

def them_nhan_vien(db, emp_id, name, age, department, skills):
    if emp_id in db:
        print("Nhân viên",emp_id,"đã tồn tại")
        return False
    db[emp_id] = {"name": name, "age": age, "department": department, "skills": skills}
    return True
    
def tim_nhan_vien_theo_id(db, emp_id):
    if emp_id in db:
        return db.get(emp_id)
    return f'Nhân viên {emp_id} không tồn tại'
    
def liet_ke_theo_phong_ban(db, department):
    list_nv = [value["name"] for key, value in db.items() if value["department"] == department]
    
    if len(list_nv) > 0:
        return f'Danh sách nhân viên thuộc phòng ban {department}: {",".join(list_nv)}'
    else:
        return f'Không có nhân viên thuộc phòng ban {department}'

def xoa_nhan_vien(db, emp_id):
    if emp_id in db:
        del db[emp_id]
        print('Xóa thành công nhân viên', emp_id)
        return True
    else:
        print('Không tồn tại mã nhân viên', emp_id)
        return False
       
them_nhan_vien(employee_db, "E01", "Ngô Mạnh Anh", 28, "AI", ["Python", "Machine Learning"]) 
them_nhan_vien(employee_db, "E01", "Ngô Mạnh Anh", 28, "AI", ["Python", "Machine Learning"])
them_nhan_vien(employee_db, "E03", "Nguyễn Linh Anh", 24, "AI", ["NLP", "LangChain"])
xoa_nhan_vien(employee_db, 'E03')

print(tim_nhan_vien_theo_id(employee_db, "E02"))
print(liet_ke_theo_phong_ban(employee_db, "AI"))

# Bạn có thể dùng các dữ liệu test này sau khi viết xong các hàm
# them_nhan_vien(employee_db, "E01", "Ngô Mạnh Anh", 28, "AI", ["Python", "Machine Learning"])
# them_nhan_vien(employee_db, "E02", "Nguyễn Thùy Linh", 25, "Data", ["SQL", "Python", "PowerBI"])
# them_nhan_vien(employee_db, "E03", "Nguyễn Linh Anh", 24, "AI", ["NLP", "LangChain"])

# print(tim_nhan_vien_theo_id(employee_db, "E02"))
# print(liet_ke_theo_phong_ban(employee_db, "AI"))
