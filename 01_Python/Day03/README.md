# Day 03 - List trong Python

## 🎯 Mục tiêu

- Nắm vững cách tạo, truy cập và thao tác với List trong Python
- Hiểu sự khác biệt giữa các phương thức thêm/xóa phần tử
- Làm việc được với Nested List (List lồng nhau)

---

## 📚 Kiến thức đã học

- **Tạo List**: `[]`, `list()`, list chứa nhiều kiểu dữ liệu, list rỗng
- **Truy cập phần tử**: Index dương, index âm, slicing `[start:stop:step]`
- **Thay đổi phần tử**: Gán trực tiếp qua index
- **Phương thức thêm**: `append()`, `insert()`, `extend()`
- **Phương thức xóa**: `remove()`, `pop()`, `del`
- **Tìm kiếm & thống kê**: `in`, `len()`, `count()`, `index()`, `max()`, `min()`, `sum()`
- **Sắp xếp**: `sort()` (in-place), `sorted()` (tạo list mới), `reverse=True`
- **Duyệt List**: `for`, `enumerate()`, `range(len())`
- **Nested List**: List lồng nhau, truy cập `list[i][j]`

---

## 💡 Điều học được (Notes)

### `append()` vs `extend()`
```python
list_a.append([4, 5])   # → [1, 2, 3, [4, 5]]  ← thêm 1 object nguyên xi
list_b.extend([4, 5])   # → [1, 2, 3, 4, 5]    ← thêm từng phần tử
```

### `sort()` vs `sorted()`
```python
nums.sort()             # Thay đổi list gốc (in-place)
sorted(nums)            # Trả về list mới, list gốc giữ nguyên
```

### `remove()` vs `pop()`
```python
list.remove("x")        # Xóa phần tử đầu tiên có giá trị "x"
list.pop()              # Xóa và trả về phần tử cuối
list.pop(i)             # Xóa và trả về phần tử tại index i
```

---

## ⚠️ Điều cần ôn lại

- `remove()` chỉ xóa lần xuất hiện **đầu tiên** — cần dùng vòng lặp nếu muốn xóa hết
- `sort()` thay đổi list gốc; hãy dùng `sorted()` khi cần giữ nguyên dữ liệu gốc
- Slicing `[::-1]` để đảo ngược nhanh mà không dùng `.reverse()`

---

## 🚀 Bài tập & Thực hành

- [x] **main.py**: Vở ghi chép — thực hành toàn bộ khái niệm List cơ bản
- [x] **exercises.py**: 7 bài tập từ cơ bản → nâng cao (slicing, thống kê, nested list)
- [x] **employee_profile.py (Mini Project)**: Hệ thống quản lý nhân viên phòng ban — dùng Nested List, hàm, thống kê lương, lọc và sắp xếp
- [x] **skill_tracker.py**: Chương trình quản lý danh sách kỹ năng đang học với input người dùng
