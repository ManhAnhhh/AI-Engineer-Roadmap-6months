# ============================================================
# Day07 - employee_profile.py
# Mini Project: Quản lý nhân sự (Lưu trữ bằng File JSON)
# ============================================================
import json
import os

DB_FILE = "employee_db.json"

# Yêu cầu:
# 1. Viết hàm `load_db()`: 
#    - Đọc dữ liệu từ file `employee_db.json` (dùng JSON load).
#    - Đặt nó trong khối Try/Except. Nếu file không tồn tại (FileNotFoundError) 
#      hoặc file trống/lỗi format (json.JSONDecodeError), hãy in ra thông báo 
#      "Khởi tạo Database rỗng" và trả về một Dictionary rỗng `{}`.
#
# 2. Viết hàm `save_db(db)`:
#    - Ghi Dictionary `db` vào file `employee_db.json` với định dạng đẹp (indent=4).
#    - Đảm bảo tham số ensure_ascii=False để lưu được tiếng Việt.
#
# 3. Viết hàm `them_nhan_vien(db, emp_id, name, age, department, skills)`:
#    - Nếu emp_id đã có, in ra báo lỗi. 
#    - Nếu chưa có, thêm vào db, SAU ĐÓ gọi luôn hàm `save_db(db)` để lưu ngay xuống ổ cứng.

# --- Viết code tại đây ---
def load_db():
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Khởi tạo Database rỗng (Không tìm thấy file hoặc file bị lỗi).")
        return {}

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

def them_nhan_vien(db, emp_id, name, age, department, skills):
    if emp_id in db:
        print(f"Lỗi: Nhân viên có mã {emp_id} đã tồn tại!")
        return False
    
    db[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "skills": skills
    }
    
    # Lưu ngay xuống ổ cứng sau khi cập nhật db (RAM)
    save_db(db)
    print(f"Đã thêm và lưu nhân viên {emp_id} thành công!")
    return True

# Kiểm thử (Hãy bỏ comment các dòng dưới đây sau khi viết xong code):
db_hien_tai = load_db()
print("Database lúc tải lên:", db_hien_tai)

them_nhan_vien(db_hien_tai, "E01", "Ngô Mạnh Anh", 28, "AI", ["Python"])
them_nhan_vien(db_hien_tai, "E02", "Nguyễn Thùy Linh", 25, "Data", ["SQL"])

# Mở file `employee_db.json` bằng VS Code để xem dữ liệu có được lưu thành công không nhé!
