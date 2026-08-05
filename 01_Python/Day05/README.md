# Day 05 - Dictionary trong Python ✅

## 🎯 Mục tiêu

- Nắm vững cấu trúc Dictionary (key-value) và phân biệt với List, Tuple, Set.
- Thành thạo các thao tác: tạo, truy cập, thêm, sửa, xóa phần tử Dictionary.
- Hiểu các phương thức quan trọng: `keys()`, `values()`, `items()`, `get()`, `pop()`, `update()`.
- Làm quen với **Nested Dictionary**, **Dict chứa List**, **List chứa Dict**.
- Viết được **Dictionary Comprehension** để xử lý dữ liệu súc tích.
- Xử lý dữ liệu kiểu **JSON** (`json.loads`, `json.dumps`) — kỹ năng cốt lõi khi làm AI/API.

---

## 📚 Kiến thức cần học

### 1. Tạo Dictionary
- Dùng `{}`: `d = {"key": "value"}`
- Dùng `dict()`: `d = dict(key="value")`
- Key phải là **Immutable** (string, int, tuple). Value là bất kỳ kiểu gì.

### 2. Truy cập & `get()`
| Cách | Hành vi khi key không tồn tại |
|------|-------------------------------|
| `d[key]` | Báo `KeyError` ❌ |
| `d.get(key)` | Trả về `None` ✅ |
| `d.get(key, default)` | Trả về `default` ✅ |

### 3. Thêm / Sửa / Xóa
| Thao tác | Cú pháp | Ghi chú |
|----------|---------|---------|
| Thêm/sửa key | `d[key] = value` | Nếu key có sẵn → ghi đè |
| Cập nhật nhiều key | `d.update({...})` | Merge dict |
| Xóa key | `del d[key]` | Báo lỗi nếu key không có |
| Xóa + lấy value | `d.pop(key)` | Báo lỗi nếu không có |
| Xóa an toàn | `d.pop(key, default)` | Không báo lỗi |

### 4. Phương thức quan trọng
- `d.keys()` — tất cả key
- `d.values()` — tất cả value
- `d.items()` — tất cả cặp `(key, value)`
- `key in d` — kiểm tra key tồn tại (O(1))

### 5. Duyệt Dictionary
```python
for key, value in d.items():   # Phổ biến nhất
    print(key, value)
```

### 6. Nested Dictionary
```python
db = {"E001": {"name": "Anh", "role": "AI Engineer"}}
db["E001"]["name"]  # Truy cập nested
```

### 7. Dictionary Comprehension
```python
squares = {n: n**2 for n in range(1, 6)}
passed  = {k: v for k, v in scores.items() if v >= 80}
```

### 8. JSON ↔ Dict
```python
import json
json_str = json.dumps(py_dict, ensure_ascii=False, indent=2)  # dict → str
py_dict  = json.loads(json_str)                               # str → dict
```

---

## 📝 Điều học được (Notes)

- **`get()` luôn an toàn hơn `d[key]`** khi không chắc key tồn tại — tránh crash chương trình.
- **`in` kiểm tra trên KEY** của dictionary, không phải value.
- **Dict là Mutable** — có thể thêm/sửa/xóa sau khi tạo.
- **List chứa Dict** là dạng dữ liệu phổ biến nhất khi làm việc với API/JSON/Database.
- **`json.dumps()`** cần `ensure_ascii=False` để giữ ký tự tiếng Việt.
- Dictionary Comprehension giúp viết code ngắn gọn hơn, tương đương `for` loop nhưng tạo dict trực tiếp.

---

## ⚠️ Điều cần ôn lại

- **`del` vs `pop()`**: `del` không trả về giá trị; `pop()` trả về giá trị đã xóa.
- **`update()` ghi đè**: Nếu key đã có trong dict gốc, `update()` sẽ ghi đè — cẩn thận khi merge.
- **Key của Dict phải Immutable**: Không thể dùng `list` làm key, nhưng có thể dùng `tuple`.
- **Thứ tự của Dict**: Từ Python 3.7+, dict giữ nguyên thứ tự chèn vào (insertion order).
- **Lưu ý nhỏ với Tuple**: Một Tuple chỉ được làm Key nếu tất cả các phần tử bên trong nó cũng là Immutable. Nếu bạn có một Tuple chứa một cái List (ví dụ: (1, 2, [3, 4])), Python vẫn sẽ cấm không cho làm Key.
- ** Comprehension **:
[ <Giá_trị_trả_về>  for  <biến>  in  <iterable>  if  <điều_kiện> ]
List thì dùng [], Dict thì dùng {} vs :, còn set dùng {} 


## 🚀 Bài tập & Thực hành

- [x] **main.py**: Lý thuyết & ví dụ minh họa đầy đủ về Dictionary.
- [x] **exercises.py**: 6 bài tập từ cơ bản đến nâng cao.
- [x] **employee_profile.py (Mini Project)**: Hệ thống quản lý hồ sơ nhân viên AI Company — CRUD, thống kê phòng ban, tìm theo kỹ năng, xuất JSON.
