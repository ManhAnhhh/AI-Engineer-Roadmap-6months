# Day 01 - Làm quen với Python

## 🎯 Mục tiêu
- Làm quen với Python, cú pháp cơ bản.
- Hiểu biến và các kiểu dữ liệu.
- Biết cách nhập xuất dữ liệu từ người dùng.
- Nắm vững cấu trúc rẽ nhánh cơ bản.

---

## 📚 Kiến thức đã học
- `print()`, `input()`
- Biến (Variable) & Kiểu dữ liệu (Data Type: `int`, `float`, `str`, `bool`)
- Ép kiểu (Type Casting)
- Toán tử cơ bản (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Cấu trúc rẽ nhánh: `if` / `elif` / `else`
- Scope (phạm vi biến) cơ bản và từ khóa `global`
- Xử lý chuỗi (String methods): `len()`, `.upper()`, `.lower()`, `.count()`, `.replace()`, `.startswith()`
- Format chuỗi: f-strings (`f"{var}"`) và căn lề (`<`, `>`, `^`)

---

## 📝 Điều học được (Notes)
- Python **không có block scope** như JavaScript (`if` và `for` không tạo scope mới).
- `def` tạo local scope.
- `global` cho phép truy cập và thay đổi biến toàn cục.
- Nối chuỗi dùng `f'{ten_bien}'` hoặc dùng `,`.
- `input()` luôn trả về kiểu chuỗi (`str`), nếu nhập số cần phải ép kiểu (ví dụ: `int()`, `float()`).

---

## ⚠️ Điều cần ôn lại
- Từ khóa `global`
- Format string (căn lề)

---

## 🚀 Bài tập & Thực hành
- [x] **exercises.py**: Các bài tập về biến, toán tử, xử lý chuỗi, tính BMI, đổi phút ra giờ.
- [x] **employee_profile.py (Mini Project)**: Xây dựng hệ thống nhập thông tin nhân viên, tính toán phụ cấp thâm niên, lương OT và in ra màn hình với giao diện được căn lề, định dạng tiền tệ đẹp mắt.