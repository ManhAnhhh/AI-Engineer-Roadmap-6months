# Day 04 - Tuple và Set trong Python

## 🎯 Mục tiêu

- Hiểu khái niệm Tuple (Immutable) và Set (Unordered, Unique).
- Sử dụng Tuple Index, Slicing, Unpacking và phân biệt với List.
- Nắm vững các thao tác tập hợp trên Set: `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`.
- Ứng dụng Tuple & Set vào bài toán làm sạch dữ liệu (Data Cleaning) thực tế trong AI/Data Science.

---

## 📚 Kiến thức cần học

### 1. Tuple (Hàng số, Không thay đổi được)
- **Đặc điểm**: Đặt trong `()`, có thứ tự (ordered), **Immutable** (không thể sửa/thêm/xóa phần tử sau khi tạo).
- **Thao tác**:
  - Access Index & Slicing: Tương tự List.
  - Unpacking: `a, b, c = (1, 2, 3)`
  - Khi nào dùng: Dữ liệu cố định (tọa độ GPS, cấu hình model, thông số không đổi).

### 2. Set (Tập hợp, Không chứa phần tử trùng lặp)
- **Đặc điểm**: Đặt trong `{}` (hoặc `set()`), **Unordered** (không có thứ tự/index), chỉ chứa các phần tử duy nhất (unique).
- **Thao tác cơ bản**:
  - `add(x)`: Thêm phần tử `x`.
  - `remove(x)`: Xóa `x` (báo lỗi KeyError nếu không có).
  - `discard(x)`: Xóa `x` (không báo lỗi nếu không có).
  - `pop()`: Lấy ngẫu nhiên 1 phần tử ra.
  - `clear()`: Xóa sạch Set.
  - `in`: Kiểm tra tồn tại với tốc độ cực nhanh $O(1)$.
- **Phép toán Tập hợp (Set Operations)**:
  - `union()` (`|`): Hợp của 2 tập hợp.
  - `intersection()` (`&`): Giao của 2 tập hợp.
  - `difference()` (`-`): Hiệu của 2 tập hợp.

---

## 📝 Điều học được (Notes)

- **Tuple**: Không thể thay đổi phần tử (Immutable). Cố tình sửa sẽ báo lỗi `TypeError`.
- Để thay đổi dữ liệu của Tuple, cần chuyển sang List bằng `list(tuple)`, sau đó thay đổi và chuyển lại thành `tuple(list)`.
- **Set**: Hàm `discard()` xoá phần tử nhưng không báo lỗi nếu phần tử đó không tồn tại, khác với `remove()` sẽ báo lỗi.
- `sorted()` luôn trả về kết quả là một List mới đã được sắp xếp, bất kể tham số truyền vào là Set hay Tuple.
- Có thể dùng Dictionary để đếm tần suất xuất hiện của các phần tử thay vì Set.

---

## ⚠️ Điều cần ôn lại
- **Iterable**: Gồm `list`, `tuple`, `set`, `string`, `dict`. Iterable có 2 kiểu là mutable và immutable:
  - **Mutable** (có thể thay đổi được sau khi tạo): `list`, `set`, `dict`.
  - **Immutable** (không thể thay đổi được sau khi tạo): `tuple`, `string`.
- **Lưu ý với Set**: Khi dùng `set`, các phần tử bên trong nó phải là những kiểu dữ liệu **immutable** (bất biến) như `string`, `number` hoặc `tuple`. (Bạn không thể bỏ một list vào bên trong set).

---

## 🚀 Bài tập & Thực hành

- [x] **main.py**: Vở ghi chép lý thuyết & ví dụ minh họa Tuple & Set.
- [x] **exercises.py**: Bài tập rèn luyện Tuple & Set từ cơ bản đến nâng cao.
- [x] **data_cleaner.py (Mini Project)**: Xử lý dữ liệu trùng lặp, lọc email/user & phân tích tệp khách hàng.
- [x] **employee_profile.py (Extra)**: AI Skill Gap Analyzer.
