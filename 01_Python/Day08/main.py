# ============================================================
# Day08 - main.py  |  AI Engineer Roadmap
# Demo code - Lập trình Hướng đối tượng (OOP) - Phần 1
# ============================================================

print("--- 1. Tạo Class và Object ---")
# Bản vẽ thiết kế (Class)
class Car:
    pass

# Tạo ra các thực thể (Objects)
xe_cua_anh = Car()
xe_cua_linh = Car()

print(type(xe_cua_anh)) # Sẽ in ra: <class '__main__.Car'>

print("\n--- 2. Hàm khởi tạo __init__ và Thuộc tính (Attributes) ---")
class Dog:
    # Hàm khởi tạo luôn luôn chạy khi một object được tạo ra
    def __init__(self, ten, giong_loai, tuoi):
        self.name = ten           # Thuộc tính name
        self.breed = giong_loai   # Thuộc tính breed
        self.age = tuoi           # Thuộc tính age

# Tạo object (truyền vào 3 đối số tương ứng với ten, giong_loai, tuoi)
cho_muc = Dog("Mực", "Chó cỏ", 3)
cho_corgi = Dog("Bánh Bao", "Corgi", 1)

# Truy cập thuộc tính
print(f"Tên chó: {cho_muc.name}, Giống: {cho_muc.breed}")
print(f"Tên chó: {cho_corgi.name}, Tuổi: {cho_corgi.age}")

print("\n--- 3. Phương thức (Methods) ---")
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        
    # Phương thức tính diện tích (Luôn phải có self)
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
        
    # Phương thức in thông tin
    def in_thong_tin(self):
        # Có thể gọi phương thức khác trong cùng class bằng cách dùng self.
        dt = self.tinh_dien_tich()
        print(f"Hình chữ nhật ({self.chieu_dai}x{self.chieu_rong}) có diện tích là {dt}")

h1 = HinhChuNhat(5, 10)
h2 = HinhChuNhat(4, 4)

h1.in_thong_tin()
h2.in_thong_tin()
