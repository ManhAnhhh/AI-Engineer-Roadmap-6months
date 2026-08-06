# Day 06 - Hàm (Functions) trong Python ✅

## 🎯 Mục tiêu
- Hiểu khái niệm Hàm (Function) và cách định nghĩa hàm với `def`.
- Phân biệt tham số (parameters) và đối số (arguments).
- Nắm vững cách sử dụng `return` và trả về nhiều giá trị.
- Thành thạo các loại đối số: Positional, Keyword, Default.
- Xử lý linh hoạt với `*args` và `**kwargs`.
- Làm quen với Hàm ẩn danh (Lambda function).

## 📚 Kiến thức cần học

### 1. Định nghĩa hàm cơ bản
```python
def greet(name):
    print(f"Hello, {name}!")
```

### 2. Lệnh `return`
- Trả về kết quả để sử dụng ở nơi khác.
- Hàm có thể trả về nhiều giá trị (dạng Tuple).

### 3. Các loại đối số (Arguments)
- **Positional**: Truyền theo đúng thứ tự.
- **Keyword**: Truyền theo tên biến (không quan tâm thứ tự).
- **Default**: Gán sẵn giá trị mặc định trong tham số.

### 4. `*args` và `**kwargs`
- `*args`: Nhận số lượng tùy ý các đối số không có tên (Positional), gom thành Tuple.
- `**kwargs`: Nhận số lượng tùy ý các đối số có tên (Keyword), gom thành Dictionary.

### 5. Hàm Lambda (Hàm ẩn danh)
- Cú pháp: `lambda args: expression`
- Thường dùng với `map()`, `filter()`, `sorted()`.

## 📝 Điều học được (Notes)
- Đã nắm được cách định nghĩa và gọi hàm cơ bản với `def` và `return`.
- Phân biệt rõ Tham số (lúc khai báo) và Đối số (lúc gọi hàm).
- Nắm được khái niệm Positional, Keyword và Default arguments.
- Sử dụng được `*args` (tuple) và `**kwargs` (dictionary) để xử lý lượng đối số linh hoạt.
- Tạm thời làm quen với Lambda function, hiểu sự khác biệt với List Comprehension.

## ⚠️ Điều chưa hiểu
- (Trống) Đã giải quyết được thắc mắc về tham số vs đối số và lambda.

## 🚀 Bài tập & Thực hành
- [x] **main.py**: Lý thuyết & ví dụ minh họa về Functions.
- [x] **exercises.py**: Các bài tập thực hành.
- [x] **employee_profile.py (Mini Project)**: Quản lý nhân viên sử dụng hàm để module hóa code.
