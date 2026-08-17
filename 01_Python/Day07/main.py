# ============================================================
# Day07 - main.py  |  AI Engineer Roadmap
# Demo code - Xử lý File & Ngoại lệ (Try/Except)
# ============================================================
import json
import os

print("--- 1. Xử lý ngoại lệ (Try - Except) ---")
def phep_chia(a, b):
    try:
        ket_qua = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except TypeError:
        print("Lỗi: Vui lòng nhập số, không nhập chữ!")
        return None
    else:
        print("Phép tính thành công!") # Chạy khi không có lỗi
        return ket_qua
    finally:
        print("Hoàn tất xử lý hàm phep_chia.\n")

print(phep_chia(10, 2))
print(phep_chia(10, 0))
print(phep_chia(10, "A"))

print("--- 2. Đọc và Ghi File Text (.txt) ---")
file_path = "demo.txt"

# Ghi file (mode 'w' - ghi đè)
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Dòng 1: Python rất thú vị!\n")
    f.write("Dòng 2: AI Engineer Roadmap.\n")
    print(f"Đã tạo file và ghi dữ liệu vào {file_path}")

# Ghi tiếp (mode 'a' - append)
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Dòng 3: Cố gắng mỗi ngày nhé!\n")

# Đọc file (mode 'r')
try:
    with open(file_path, "r", encoding="utf-8") as f:
        print("\nNội dung file demo.txt:")
        for line in f:
            print(line.strip()) # strip() để xóa dấu xuống dòng dư thừa
except FileNotFoundError:
    print("File không tồn tại!")

print("\n--- 3. Đọc và Ghi File JSON ---")
json_path = "data.json"
user_data = {
    "name": "Ngô Mạnh Anh",
    "role": "AI Engineer",
    "skills": ["Python", "Machine Learning"]
}

# Ghi vào file JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=4)
    print(f"Đã lưu dữ liệu Dictionary vào {json_path}")

# Đọc từ file JSON
with open(json_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("Dữ liệu đọc được từ JSON:")
    print(type(loaded_data))
    print(loaded_data)

# Chú ý: 
# Nếu bạn muốn giữ lại file demo để xem, có thể comment 4 dòng code dọn dẹp bên dưới lại.
if os.path.exists(file_path):
    os.remove(file_path)
if os.path.exists(json_path):
    os.remove(json_path)
