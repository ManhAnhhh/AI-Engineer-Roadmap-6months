# ============================================================
# Day 05 - employee_profile.py  |  AI Engineer Roadmap
# Mini Project: Hệ thống quản lý hồ sơ nhân viên AI Company
# ============================================================
#
# Mô tả:
#   Xây dựng một hệ thống đơn giản để quản lý hồ sơ nhân viên
#   của một công ty AI. Hệ thống cần làm được:
#   - Lưu trữ thông tin nhân viên dưới dạng Dictionary
#   - Tìm kiếm nhân viên theo ID
#   - Thêm nhân viên mới
#   - Cập nhật thông tin nhân viên
#   - Thống kê theo phòng ban
#   - Xuất báo cáo dạng JSON
# ============================================================

import json

# ============================================================
# DỮ LIỆU BAN ĐẦU
# ============================================================
company_db = {
    "E001": {
        "name": "Ngô Mạnh Anh",
        "role": "AI Engineer",
        "department": "Research",
        "salary": 18000000,
        "skills": ["Python", "PyTorch", "LangChain"],
        "performance": 95
    },
    "E002": {
        "name": "Nguyễn Thùy Linh",
        "role": "Data Scientist",
        "department": "Data",
        "salary": 16000000,
        "skills": ["Python", "SQL", "Pandas", "Scikit-learn"],
        "performance": 88
    },
    "E003": {
        "name": "Trần Minh Quân",
        "role": "MLOps Engineer",
        "department": "Infrastructure",
        "salary": 20000000,
        "skills": ["Docker", "Kubernetes", "CI/CD", "Python"],
        "performance": 82
    },
    "E004": {
        "name": "Lê Thị Hoa",
        "role": "AI Product Manager",
        "department": "Product",
        "salary": 22000000,
        "skills": ["Product Management", "AI Strategy", "Jira"],
        "performance": 90
    },
    "E005": {
        "name": "Phạm Văn Đức",
        "role": "Data Engineer",
        "department": "Data",
        "salary": 17000000,
        "skills": ["Python", "Spark", "Airflow", "SQL"],
        "performance": 78
    },
}


# ============================================================
# FUNCTION 1: Tìm kiếm nhân viên theo ID
# ============================================================
def find_employee(db: dict, emp_id: str) -> dict | None:
    """Tìm kiếm nhân viên theo ID. Trả về thông tin hoặc None."""
    return db.get(emp_id, None)


# ============================================================
# FUNCTION 2: Thêm nhân viên mới
# ============================================================
def add_employee(db: dict, emp_id: str, info: dict) -> bool:
    """Thêm nhân viên mới. Trả về False nếu ID đã tồn tại."""
    if emp_id in db:
        print(f"  ⚠️  ID '{emp_id}' đã tồn tại!")
        return False
    db[emp_id] = info
    print(f"  ✅  Đã thêm nhân viên '{info['name']}' với ID {emp_id}.")
    return True


# ============================================================
# FUNCTION 3: Cập nhật thông tin nhân viên
# ============================================================
def update_employee(db: dict, emp_id: str, updates: dict) -> bool:
    """Cập nhật một hoặc nhiều trường của nhân viên."""
    if emp_id not in db:
        print(f"  ❌  Không tìm thấy nhân viên ID '{emp_id}'.")
        return False
    db[emp_id].update(updates)
    print(f"  ✅  Đã cập nhật thông tin nhân viên '{db[emp_id]['name']}'.")
    return True


# ============================================================
# FUNCTION 4: Thống kê theo phòng ban
# ============================================================
def department_stats(db: dict) -> dict:
    """
    Trả về dict thống kê theo phòng ban:
    {department: {"count": int, "avg_salary": float, "avg_performance": float}}
    """
    stats = {}
    for emp_id, info in db.items():
        dept = info["department"]
        if dept not in stats:
            stats[dept] = {"count": 0, "total_salary": 0, "total_performance": 0}
        stats[dept]["count"] += 1
        stats[dept]["total_salary"] += info["salary"]
        stats[dept]["total_performance"] += info["performance"]

    # Tính trung bình
    result = {}
    for dept, data in stats.items():
        count = data["count"]
        result[dept] = {
            "count": count,
            "avg_salary": round(data["total_salary"] / count),
            "avg_performance": round(data["total_performance"] / count, 1),
        }
    return result


# ============================================================
# FUNCTION 5: Tìm nhân viên có performance cao nhất
# ============================================================
def top_performer(db: dict) -> tuple:
    """Trả về (emp_id, info) của nhân viên có performance cao nhất."""
    best_id = max(db, key=lambda eid: db[eid]["performance"])
    return best_id, db[best_id]


# ============================================================
# FUNCTION 6: Tìm tất cả nhân viên biết một kỹ năng cụ thể
# ============================================================
def find_by_skill(db: dict, skill: str) -> list:
    """Trả về list các nhân viên có kỹ năng đã cho."""
    return [
        {"id": eid, "name": info["name"], "role": info["role"]}
        for eid, info in db.items()
        if skill in info["skills"]
    ]


# ============================================================
# FUNCTION 7: Xuất báo cáo JSON
# ============================================================
def export_report(db: dict, filename: str = "employee_report.json"):
    """Xuất toàn bộ database ra file JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"  ✅  Đã xuất báo cáo ra file '{filename}'.")


# ============================================================
# MAIN — Chạy thử hệ thống
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("    🏢  AI COMPANY — EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 60)

    # --- Test 1: Tìm kiếm nhân viên ---
    print("\n📌 [1] Tìm kiếm nhân viên ID E001:")
    emp = find_employee(company_db, "E001")
    if emp:
        print(f"  Tên   : {emp['name']}")
        print(f"  Vai trò: {emp['role']}")
        print(f"  Lương  : {emp['salary']:,} VND")
        print(f"  Skills : {', '.join(emp['skills'])}")

    print("\n📌 [1b] Tìm kiếm nhân viên ID E999 (không tồn tại):")
    emp_none = find_employee(company_db, "E999")
    print(f"  Kết quả: {emp_none}")

    # --- Test 2: Thêm nhân viên ---
    print("\n📌 [2] Thêm nhân viên mới:")
    add_employee(company_db, "E006", {
        "name": "Hoàng Anh Vũ",
        "role": "LLM Researcher",
        "department": "Research",
        "salary": 25000000,
        "skills": ["Python", "PyTorch", "Transformers", "RLHF"],
        "performance": 97
    })
    # Thử thêm ID đã tồn tại
    add_employee(company_db, "E001", {"name": "Người Trùng Tên"})

    # --- Test 3: Cập nhật thông tin ---
    print("\n📌 [3] Cập nhật thông tin nhân viên E002:")
    update_employee(company_db, "E002", {"salary": 19000000, "performance": 92})
    updated = find_employee(company_db, "E002")
    print(f"  Lương mới: {updated['salary']:,} VND")
    print(f"  Performance mới: {updated['performance']}")

    # --- Test 4: Thống kê phòng ban ---
    print("\n📌 [4] Thống kê theo phòng ban:")
    stats = department_stats(company_db)
    print(f"  {'Phòng ban':<20} {'Nhân viên':>10} {'Lương TB':>15} {'Perf TB':>10}")
    print("  " + "-" * 60)
    for dept, data in stats.items():
        print(f"  {dept:<20} {data['count']:>10} {data['avg_salary']:>15,} {data['avg_performance']:>10}")

    # --- Test 5: Top performer ---
    print("\n📌 [5] Nhân viên xuất sắc nhất:")
    top_id, top_info = top_performer(company_db)
    print(f"  🏆  {top_info['name']} (ID: {top_id}) — Performance: {top_info['performance']}")

    # --- Test 6: Tìm theo kỹ năng ---
    print("\n📌 [6] Nhân viên biết 'Python':")
    python_devs = find_by_skill(company_db, "Python")
    for dev in python_devs:
        print(f"  - [{dev['id']}] {dev['name']} ({dev['role']})")

    # --- Test 7: Xuất JSON ---
    print("\n📌 [7] Xuất báo cáo JSON:")
    export_report(company_db, "employee_report.json")

    # --- Bonus: Dictionary Comprehension để tạo bảng tổng hợp ---
    print("\n📌 [Bonus] Bảng lương tổng hợp (Comprehension):")
    salary_table = {
        info["name"]: f"{info['salary']:,} VND"
        for eid, info in company_db.items()
    }
    for name, salary in salary_table.items():
        print(f"  {name:<25} → {salary}")

    print("\n" + "=" * 60)
    print("✅  Hệ thống chạy thành công!")
    print("=" * 60)