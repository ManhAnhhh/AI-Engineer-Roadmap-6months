# ============================================================
# Day 01 - Mini Project: employee_profile.py
# Tên dự án: Hệ thống Hồ Sơ Nhân Viên
# ============================================================
#
# MÔ TẢ:
#   Xây dựng chương trình nhập thông tin nhân viên,
#   tính toán lương thực nhận và hiển thị hồ sơ đẹp ra màn hình.
#
# ============================================================
# BƯỚC 1: Nhập thông tin nhân viên
# ============================================================
# Dùng input() để nhận các thông tin sau từ người dùng:
#   - ho_ten       : họ và tên (str)
#   - tuoi         : tuổi (int)
#   - phong_ban    : tên phòng ban (str)
#   - nam_kn       : số năm kinh nghiệm (int)
#   - luong_cb     : lương cơ bản (float, đơn vị: triệu VND)
#   - gio_lam_them : số giờ làm thêm trong tháng (float)
#
# ============================================================
# BƯỚC 2: Tính toán
# ============================================================
# 2.1. Xếp loại nhân viên theo số năm kinh nghiệm:
#       < 2 năm  -> "Junior"
#       2-5 năm  -> "Mid-level"
#       > 5 năm  -> "Senior"
#
# 2.2. Phụ cấp thâm niên (tính theo % lương cơ bản):
#       Junior    ->  0%
#       Mid-level -> 10%
#       Senior    -> 20%
#
# 2.3. Lương làm thêm:
#       Công thức: gio_lam_them × (luong_cb / 26 / 8) × 1.5
#       (1 tháng = 26 ngày công, 1 ngày = 8 tiếng, hệ số OT = 1.5)
#
# 2.4. Tổng lương thực nhận:
#       tong_luong = luong_cb + phu_cap + luong_lam_them
#
# ============================================================
# BƯỚC 3: Hiển thị hồ sơ
# ============================================================
# In ra màn hình theo định dạng sau (căn chỉnh đẹp):
#
# ╔══════════════════════════════════╗
#         HỒ SƠ NHÂN VIÊN
# ╚══════════════════════════════════╝
#  Họ tên      : Nguyễn Mạnh Anh
#  Tuổi        : 23
#  Phòng ban   : AI Engineering
#  Kinh nghiệm : 1 năm  →  Junior
# ──────────────────────────────────
#  Lương cơ bản      : 8,000,000 đ
#  Phụ cấp thâm niên :         0 đ
#  Lương làm thêm    :   750,000 đ
# ──────────────────────────────────
#  TỔNG LƯƠNG        : 8,750,000 đ
# ══════════════════════════════════
#
# Gợi ý định dạng số: f"{so:,.0f}" sẽ in ra "8,000,000"
#
# ============================================================
# BƯỚC 4: Thử thách thêm (nếu muốn)
# ============================================================
# - Kiểm tra đầu vào: tuổi phải từ 18-65, lương > 0, giờ OT >= 0
#   Nếu không hợp lệ -> in thông báo lỗi và dừng chương trình.
# - Tính số phút làm thêm (dùng lại kiến thức Bài 7):
#   In ra: "Tổng thời gian OT: X giờ Y phút"

# ============================================================
# --- Viết code tại đây ---
# ============================================================


ho_ten = input('Nhập họ tên: ')
tuoi = int(input('Nhập tuổi: '))
phong_ban = input('Nhập phòng ban: ')
so_nam_kn = float(input('Số năm kinh nghiệm: '))
luong_co_ban = float(input('Lương cơ bản: '))
gio_lam_them = float(input('Giờ làm thêm: '))
phu_cap = 0
luong_lam_them = 0
xep_loai = ""

# Xác định cấp bậc và phụ cấp
if so_nam_kn < 2:
    xep_loai = 'Junior'
    phu_cap = 0
elif 2 <= so_nam_kn <= 5:
    xep_loai = 'Mid-level'
    phu_cap = luong_co_ban * 0.1  # 10/100 viết gọn là 0.1
else:
    xep_loai = 'Senior'
    phu_cap = luong_co_ban * 0.2  # 20/100

# Tính toán
luong_lam_them = gio_lam_them * (luong_co_ban / 26 / 8) * 1.5
tong_luong = luong_co_ban + phu_cap + luong_lam_them

# In Hồ Sơ
print("\n╔══════════════════════════════════╗")
print("        HỒ SƠ NHÂN VIÊN")
print("╚══════════════════════════════════╝")
print(f" Họ tên      : {ho_ten}")
print(f" Tuổi        : {tuoi}")
print(f" Phòng ban   : {phong_ban}")
print(f" Kinh nghiệm : {so_nam_kn} năm  →  {xep_loai}")
print("──────────────────────────────────")
print(f" Lương cơ bản      : {luong_co_ban:>10,.0f} đ")
print(f" Phụ cấp thâm niên : {phu_cap:>10,.0f} đ")
print(f" Lương làm thêm    : {luong_lam_them:>10,.0f} đ")
print("──────────────────────────────────")
print(f" TỔNG LƯƠNG        : {tong_luong:>10,.0f} đ")
print("══════════════════════════════════")
