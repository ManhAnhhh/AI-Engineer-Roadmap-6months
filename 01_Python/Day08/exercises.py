# ============================================================
# Day08 - exercises.py
# Bài tập: Lập trình Hướng đối tượng (Class)
# ============================================================

# ------------------------------------------------------------
# Bài 1: Lớp Tài khoản ngân hàng (BankAccount)
# 1. Tạo một class `BankAccount`.
# 2. Có hàm `__init__` nhận vào `chu_tai_khoan` và `so_du` (mặc định so_du = 0).
# 3. Tạo phương thức `gui_tien(self, so_tien)`: Cộng tiền vào `so_du` và in ra "Đã nạp [x] VND".
# 4. Tạo phương thức `rut_tien(self, so_tien)`: Nếu `so_tien` <= `so_du` thì trừ đi và in ra thành công. Ngược lại in ra "Số dư không đủ".
# ------------------------------------------------------------
# --- Viết code tại đây ---
class BankAccount:
    def __init__(self, chu_tai_khoan, so_du = 0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
    def gui_tien(self, so_tien):
        self.so_du += so_tien
        print('Đã nạp', so_tien, 'VND')
    def rut_tien(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print("Trừ tiền thành công")
        else:
            print("Số dư không đủ")

# Kiểm thử Bài 1 (Hãy bỏ comment khi chạy):
# tk = BankAccount("Ngô Mạnh Anh", 1000)
# print(f"Số tiền ban đầu của {tk.chu_tai_khoan} là: {tk.so_du}")
# tk.gui_tien(500)
# tk.rut_tien(2000) # Số dư không đủ
# tk.rut_tien(1000)
# print(f"Số tiền sau khi thự hiện gửi/rút tiền của {tk.chu_tai_khoan} là: {tk.so_du}")


# ------------------------------------------------------------
# Bài 2: Quản lý Sách (Book)
# 1. Tạo class `Book` với các thuộc tính: `tieu_de`, `tac_gia`, `nam_xuat_ban`.
# 2. Viết phương thức `thong_tin_sach(self)` để trả về chuỗi (string): 
#    "Cuốn sách [tieu_de] được viết bởi [tac_gia] vào năm [nam_xuat_ban]".
# 3. Khởi tạo 2 đối tượng sách và in thông tin của chúng ra màn hình.
# ------------------------------------------------------------
# --- Viết code tại đây ---

class Book:
    def __init__(self, tieu_de, tac_gia, nam_xuat_ban):
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
    def thong_tin_sach(self):
        return f"Cuốn sách {self.tieu_de} được viết bởi {self.tac_gia} vào năm {self.nam_xuat_ban}"
        
sach1 = Book('Doremon', 'Fukuki', 2020)
sach2 = Book('Goku', 'NoName', '2019a')

print(sach1.thong_tin_sach())
print(sach2.thong_tin_sach())





