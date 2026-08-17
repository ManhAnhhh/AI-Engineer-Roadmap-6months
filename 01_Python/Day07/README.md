# Day 07 - Xử lý File & Ngoại lệ (File & Exception Handling) ✅

## 🎯 Mục tiêu
- Nắm vững cách bắt và xử lý lỗi (Exception Handling) với `try`, `except`, `else`, `finally`.
- Hiểu cách Python báo lỗi để debug dễ dàng hơn.
- Biết cách mở, đọc, và ghi file văn bản (`.txt`) bằng cú pháp `with open(...)`.
- Làm quen với việc xử lý file CSV và JSON.
- Biết cách lưu trữ dữ liệu vĩnh viễn xuống ổ cứng thay vì chỉ lưu trên RAM (biến).

## 📚 Kiến thức cần học

### 1. Xử lý ngoại lệ (Try - Except)
Khi code có lỗi (chia cho 0, mở file không tồn tại, sai kiểu dữ liệu), chương trình sẽ bị dừng (crash). Ta dùng `try...except` để "bắt" lỗi và cho chương trình chạy tiếp.
```python
try:
    # Code có thể sinh ra lỗi
    ket_qua = 10 / 0
except ZeroDivisionError:
    # Chạy khi lỗi cụ thể xảy ra
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    # Bắt tất cả các lỗi khác
    print(f"Lỗi không xác định: {e}")
else:
    # Chạy khi không có lỗi
    print("Phép tính thành công!")
finally:
    # Luôn luôn chạy, dù có lỗi hay không (Thường dùng để đóng file/kết nối)
    print("Kết thúc xử lý.")
```

### 2. Làm việc với File văn bản (`.txt`)
Luôn dùng từ khóa `with` để mở file, vì nó sẽ **tự động đóng file** sau khi dùng xong (kể cả khi bị lỗi).
Các chế độ (mode) mở file:
- `'r'` (Read): Chỉ đọc (Mặc định). Báo lỗi nếu file không tồn tại.
- `'w'` (Write): Ghi đè. Xóa hết nội dung cũ, tạo file mới nếu chưa có.
- `'a'` (Append): Ghi tiếp vào cuối file. Không xóa nội dung cũ.

```python
# Ghi file
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào AI Engineer!")

# Đọc file
with open("data.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
```

### 3. Làm việc với JSON
Như đã nhắc ở Day 05, JSON là chuẩn dữ liệu rất phổ biến. Ta có thể lưu Dictionary thẳng vào file JSON.
- `json.dump(data, file)`: Ghi dictionary vào file.
- `json.load(file)`: Đọc file JSON và chuyển thành dictionary.

## 📝 Điều học được (Notes)
- **Phân biệt cực dễ về JSON:**

  *Dùng với Chuỗi (String): CÓ chữ `s` (viết tắt của string)*
  - `json.dumps(dict)`: Đổ dữ liệu từ Dictionary thành một chuỗi JSON.
  - `json.loads(chuoi_json)`: Nạp một chuỗi JSON thành Dictionary.

  *Dùng trực tiếp với File (Tệp tin): KHÔNG CÓ chữ `s`*
  - `json.dump(dict, file)`: Đổ dữ liệu thẳng vào một file lưu trên ổ cứng.
  - `json.load(file)`: Đọc và nạp dữ liệu thẳng từ một file lưu trên ổ cứng thành Dictionary.

- **Phân biệt `f.read()` và `json.load(f)`:**
  - `f.read()`: Đọc toàn bộ file và trả về một **Chuỗi (String) thuần túy**. Bạn không thể truy xuất dữ liệu kiểu `[key]` được.
  - `json.load(f)`: Đọc file JSON và tự động **chuyển đổi nó thành Dictionary/List** của Python để thao tác dữ liệu. Thực chất, `json.load(f)` ngầm gọi `f.read()` bên trong nó rồi mới dịch thành Dictionary.
  - *(Lưu ý: Không có hàm `json.read()` trong thư viện json của Python).*

## ⚠️ Điều chưa hiểu
- (Trống) Đã giải quyết được sự khác biệt giữa đọc file thường và file JSON.

## 🚀 Bài tập & Thực hành
- [ ] **main.py**: Lý thuyết & ví dụ minh họa.
- [ ] **exercises.py**: Bài tập thực hành Try/Except và đọc ghi file cơ bản.
- [ ] **employee_profile.py (Mini Project)**: Nâng cấp hệ thống! Đọc/ghi dữ liệu nhân viên từ file JSON để bảo toàn dữ liệu khi tắt chương trình.
