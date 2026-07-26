# ============================================================
# Day 03 - employee_profile.py  |  AI Engineer Roadmap
# Mini Project: Hệ thống Quản lý Danh sách Nhân viên Phòng ban
# ============================================================
# Mô tả:
#   Xây dựng hệ thống quản lý nhân viên đơn giản sử dụng List.
#   Hệ thống cho phép:
#     - Lưu trữ danh sách nhân viên (dạng nested list).
#     - Thêm nhân viên mới.
#     - Xóa nhân viên theo tên.
#     - Hiển thị danh sách đẹp với thứ tự.
#     - Thống kê lương: trung bình, cao nhất, thấp nhất.
# ============================================================

# -------------------------------------------------------
# DỮ LIỆU NHÂN VIÊN
# Mỗi nhân viên: [Họ tên, Chức vụ, Phòng ban, Lương (triệu)]
# -------------------------------------------------------
nhan_vien = [
    ["Nguyễn Văn An",    "Senior Dev",    "Kỹ thuật",    25],
    ["Trần Thị Bình",    "Product Manager","Sản phẩm",   30],
    ["Lê Hoàng Chi",     "Junior Dev",    "Kỹ thuật",    15],
    ["Phạm Minh Dũng",   "Data Analyst",  "Dữ liệu",     20],
    ["Hoàng Thị Lan",    "UI/UX Designer","Thiết kế",    22],
    ["Đỗ Quang Minh",    "DevOps",        "Kỹ thuật",    28],
]

# -------------------------------------------------------
# HÀM IN TIÊU ĐỀ BẢNG
# -------------------------------------------------------
def in_tieu_de():
    print("=" * 65)
    print(f"{'HỆ THỐNG QUẢN LÝ NHÂN VIÊN':^65}")
    print("=" * 65)

# -------------------------------------------------------
# HÀM HIỂN THỊ DANH SÁCH NHÂN VIÊN
# -------------------------------------------------------
def hien_thi_danh_sach(ds):
    print(f"\n{'STT':<5} {'Họ và tên':<22} {'Chức vụ':<18} {'Phòng ban':<14} {'Lương'}")
    print("-" * 65)
    for i, nv in enumerate(ds, start=1):
        ten, chuc_vu, phong_ban, luong = nv
        print(f"{i:<5} {ten:<22} {chuc_vu:<18} {phong_ban:<14} {luong} triệu")
    print(f"\n📊 Tổng số nhân viên: {len(ds)} người")

# -------------------------------------------------------
# HÀM THỐNG KÊ LƯƠNG
# -------------------------------------------------------
def thong_ke_luong(ds):
    luong_list = [nv[3] for nv in ds]      # Lấy cột lương từ nested list
    tb = sum(luong_list) / len(luong_list)

    luong_cao_nhat = max(luong_list)
    luong_thap_nhat = min(luong_list)

    # Tìm tên nhân viên lương cao nhất
    for nv in ds:
        if nv[3] == luong_cao_nhat:
            ten_cao = nv[0]
        if nv[3] == luong_thap_nhat:
            ten_thap = nv[0]

    print("\n💰 THỐNG KÊ LƯƠNG:")
    print(f"   Lương trung bình : {tb:.1f} triệu")
    print(f"   Lương cao nhất   : {luong_cao_nhat} triệu ({ten_cao})")
    print(f"   Lương thấp nhất  : {luong_thap_nhat} triệu ({ten_thap})")

# -------------------------------------------------------
# HÀM THÊM NHÂN VIÊN
# -------------------------------------------------------
def them_nhan_vien(ds, ten, chuc_vu, phong_ban, luong):
    nv_moi = [ten, chuc_vu, phong_ban, luong]
    ds.append(nv_moi)
    print(f"\n✅ Đã thêm nhân viên: {ten} ({chuc_vu} - {phong_ban})")

# -------------------------------------------------------
# HÀM XÓA NHÂN VIÊN THEO TÊN
# -------------------------------------------------------
def xoa_nhan_vien(ds, ten_can_xoa):
    for nv in ds:
        if nv[0] == ten_can_xoa:
            ds.remove(nv)
            print(f"\n🗑️  Đã xóa nhân viên: {ten_can_xoa}")
            return
    print(f"\n⚠️  Không tìm thấy nhân viên: {ten_can_xoa}")

# -------------------------------------------------------
# HÀM LỌC NHÂN VIÊN THEO PHÒNG BAN
# -------------------------------------------------------
def loc_theo_phong_ban(ds, phong_ban):
    ket_qua = []
    for nv in ds:
        if nv[2] == phong_ban:
            ket_qua.append(nv)
    return ket_qua

# -------------------------------------------------------
# CHƯƠNG TRÌNH CHÍNH
# -------------------------------------------------------
in_tieu_de()

# --- Hiển thị toàn bộ danh sách ---
print("\n📋 DANH SÁCH NHÂN VIÊN HIỆN TẠI:")
hien_thi_danh_sach(nhan_vien)

# --- Thống kê lương ---
thong_ke_luong(nhan_vien)

# --- Thêm nhân viên mới ---
print("\n" + "─" * 65)
print("➕ THÊM NHÂN VIÊN MỚI")
them_nhan_vien(nhan_vien, "Bùi Thị Hoa", "QA Engineer", "Kỹ thuật", 18)

# --- Hiển thị sau khi thêm ---
print("\n📋 DANH SÁCH SAU KHI THÊM:")
hien_thi_danh_sach(nhan_vien)

# --- Lọc theo phòng ban ---
print("\n" + "─" * 65)
print("🔍 LỌC NHÂN VIÊN PHÒNG KỸ THUẬT:")
phong_kt = loc_theo_phong_ban(nhan_vien, "Kỹ thuật")
hien_thi_danh_sach(phong_kt)

# --- Xóa nhân viên ---
print("\n" + "─" * 65)
print("❌ XÓA NHÂN VIÊN")
xoa_nhan_vien(nhan_vien, "Lê Hoàng Chi")
xoa_nhan_vien(nhan_vien, "Nguyễn Văn Không Có")  # Tên không tồn tại

# --- Danh sách cuối cùng sau khi xóa ---
print("\n📋 DANH SÁCH SAU KHI XÓA:")
hien_thi_danh_sach(nhan_vien)
thong_ke_luong(nhan_vien)

# --- Sắp xếp theo lương giảm dần ---
print("\n" + "─" * 65)
print("📈 DANH SÁCH SẮP XẾP THEO LƯƠNG (GIẢM DẦN):")
nhan_vien_sort = sorted(nhan_vien, key=lambda nv: nv[3], reverse=True)
hien_thi_danh_sach(nhan_vien_sort)

print("\n" + "=" * 65)
print(f"{'KẾT THÚC CHƯƠNG TRÌNH':^65}")
print("=" * 65)
