# Day 08 - Lập trình Hướng đối tượng (OOP - Phần 1) ✅

## 🎯 Mục tiêu
- Hiểu khái niệm OOP (Object-Oriented Programming).
- Phân biệt được Lớp (Class) và Đối tượng (Object).
- Biết cách khai báo một Class trong Python bằng từ khóa `class`.
- Nắm vững hàm khởi tạo `__init__` và vai trò của từ khóa `self`.
- Tạo và truy cập Thuộc tính (Attributes) & Phương thức (Methods).

## 📚 Kiến thức cần học

### 1. Class và Object là gì?
- **Class (Lớp):** Là bản vẽ thiết kế (Ví dụ: Bản vẽ xe ô tô).
- **Object (Đối tượng):** Là thực thể cụ thể được tạo ra từ bản vẽ đó (Ví dụ: Xe ô tô Vinfast VF8 màu trắng).

### 2. Khai báo Class và tạo Object
```python
# Tạo class
class NhanVien:
    pass

# Tạo object (instance) từ class
nv1 = NhanVien()
nv2 = NhanVien()
```

### 3. Hàm khởi tạo `__init__` và từ khóa `self`
Khi tạo một object, hàm `__init__` sẽ tự động chạy đầu tiên để "khởi tạo" dữ liệu ban đầu cho object đó.
Từ khóa `self` đại diện cho chính cái object đang được xử lý.
```python
class NhanVien:
    def __init__(self, ten, tuoi):
        self.ten = ten     # Thuộc tính (Attribute)
        self.tuoi = tuoi

nv1 = NhanVien("Mạnh Anh", 28)
print(nv1.ten)  # In ra: Mạnh Anh
```

### 4. Phương thức (Method)
Phương thức thực chất là một **Hàm (Function)** nằm bên trong một Class. Nó mô tả hành động của đối tượng. Tất cả các phương thức trong class đều phải có `self` làm tham số đầu tiên.
```python
class NhanVien:
    def __init__(self, ten):
        self.ten = ten
        
    def chao_hoi(self):
        print(f"Xin chào, tôi là {self.ten}")

nv1 = NhanVien("Mạnh Anh")
nv1.chao_hoi()
```

## 📝 Điều học được (Notes)
- **Truy cập phần tử:**
  - `Dùng ngoặc vuông []`: Khi bạn muốn mở một "thùng chứa" dữ liệu (List, Dictionary) để tra cứu theo Key hoặc Index. Không được dùng `class["key"]`.
  - `Dùng dấu chấm .`: Khi bạn muốn trỏ vào một "đối tượng sống" (Class Object) để lấy đặc điểm (Thuộc tính / Attribute) hoặc bảo nó làm việc (Hàm / Method). Phải dùng `class.key`.

- **Hàm khởi tạo `__init__` và Tham số:**
  - Khi tạo object từ class, phải truyền ĐỦ tham số tương ứng trong `__init__` (trừ `self`).
  - Nếu muốn linh hoạt, có thể gán giá trị mặc định (`default_value`).
    Ví dụ:
    ```python
    class BankAccount:
        def __init__(self, chu_tai_khoan, so_du = 0):
            self.chu_tai_khoan = chu_tai_khoan
            self.so_du = so_du
    ```
    Khi gọi `tk = BankAccount("ManhAnh")` sẽ không lỗi vì `so_du` tự động là 0.
    Khi gọi `tk2 = BankAccount("Linh", 100)` thì `so_du` sẽ là 100.
  - Nếu tham số không có `default_value` mà không truyền vào, Python sẽ báo lỗi ngay lập tức.

## ⚠️ Điều chưa hiểu
- (Trống) Các ghi chú xuất sắc đã được chuyển lên phần Điều học được.

## 🚀 Bài tập & Thực hành
- [x] **main.py**: Lý thuyết & ví dụ minh họa cơ bản về Class.
- [x] **exercises.py**: Các bài tập thiết kế Class cơ bản.
- [x] **employee_profile.py (Mini Project)**: Tái cấu trúc lại dữ liệu! Thay vì dùng Dictionary cho mỗi nhân viên, hãy tạo class `Employee`.
