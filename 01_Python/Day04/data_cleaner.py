# ============================================================
# Day 04 - data_cleaner.py  |  AI Engineer Roadmap
# Mini Project: Hệ thống Làm sạch & Phân tích Tập dữ liệu Khách hàng
# ============================================================
# Mô tả:
#   Trong AI & Data Science, làm sạch dữ liệu (Data Cleaning) là bước quan trọng nhất.
#   Dự án này mô phỏng quá trình xử lý log truy cập & danh sách khách hàng:
#     - Sử dụng Tuple để lưu bản ghi thông tin cố định (User ID, Name, Email, Role).
#     - Sử dụng Set để lọc dữ liệu trùng lặp (Duplicate removal).
#     - Sử dụng các phép toán Set (Union, Intersection, Difference) để phân tích tập khách hàng.
# ============================================================

# 1. DỮ LIỆU ĐẦU VÀO (Thường bị lặp do ghi log hệ thống)
# Mỗi record dạng Tuple: (User_ID, Name, Email)
raw_logs = [
    ("U001", "Ngô Mạnh Anh", "manhanh@gmail.com"),
    ("U002", "Nguyễn Thùy Linh", "thuylinh@gmail.com"),
    ("U001", "Ngô Mạnh Anh", "manhanh@gmail.com"),  # Trùng lặp
    ("U003", "Trần Thị Bình", "binh.tran@yahoo.com"),
    ("U004", "Lê Hoàng Chi", "chi.le@gmail.com"),
    ("U002", "Nguyễn Thùy Linh", "thuylinh@gmail.com"),  # Trùng lặp
    ("U005", "Phạm Minh Dũng", "dung.pham@gmail.com"),
]

# Danh sách khách hàng đã mua hàng trong Tháng 1 và Tháng 2 (chỉ lưu User_ID)
purchases_jan = {"U001", "U002", "U003", "U006"}
purchases_feb = {"U002", "U004", "U005", "U006"}

# -------------------------------------------------------
# HÀM HIỂN THỊ TIÊU ĐỀ
# -------------------------------------------------------
def in_tieu_de(title):
    print("\n" + "=" * 65)
    print(f"{title:^65}")
    print("=" * 65)

# -------------------------------------------------------
# HÀM LÀM SẠCH DỮ LIỆU LOG (DÙNG SET)
# -------------------------------------------------------
def lam_sach_logs(logs):
    # Set tự động loại bỏ các Tuple bị trùng lặp hoàn toàn
    clean_set = set(logs)
    return list(clean_set)

# -------------------------------------------------------
# CHƯƠNG TRÌNH CHÍNH
# -------------------------------------------------------
in_tieu_de("HỆ THỐNG LÀM SẠCH & PHÂN TÍCH DỮ LIỆU")

# --- Bước 1: Xử lý dữ liệu trùng lặp ---
print(f"📊 Số lượng bản ghi log ban đầu: {len(raw_logs)}")

cleaned_logs = lam_sach_logs(raw_logs)
print(f"✅ Số lượng bản ghi sau khi làm sạch (Unique): {len(cleaned_logs)}")

print("\n📋 DANH SÁCH USER DUY NHẤT:")
print(f"{'ID':<8} {'Họ và tên':<20} {'Email'}")
print("-" * 55)
for user in cleaned_logs:
    user_id, name, email = user  # Tuple Unpacking
    print(f"{user_id:<8} {name:<20} {email}")

# --- Bước 2: Phân tích tập khách hàng bằng Phép toán Set ---
in_tieu_de("PHÂN TÍCH HÀNH VI MUA HÀNG (SET OPERATIONS)")

# 1. Khách hàng mua hàng ở CẢ 2 THÁNG (Intersection)
loyal_customers = purchases_jan.intersection(purchases_feb)
print("1. Khách hàng trung thành (Mua cả T1 và T2):", loyal_customers)

# 2. Tất cả khách hàng đã mua hàng ít nhất 1 lần (Union)
all_buyers = purchases_jan | purchases_feb
print("2. Tổng số khách hàng từng mua hàng (T1 ∪ T2):", all_buyers)

# 3. Khách hàng CHỈ mua vào Tháng 1 mà KHÔNG mua ở Tháng 2 (Difference)
churned_jan = purchases_jan - purchases_feb
print("3. Khách hàng mua T1 nhưng dừng mua ở T2:", churned_jan)

# 4. Khách hàng MỚI phát sinh ở Tháng 2 (Difference)
new_feb = purchases_feb - purchases_jan
print("4. Khách hàng mới ở Tháng 2:", new_feb)

# --- Bước 3: Kiểm tra tra cứu nhanh với `in` ---
in_tieu_de("TRA CỨU NHANH HỆ THỐNG")
check_user = "U001"
if check_user in all_buyers:
    print(f"🔍 User '{check_user}' đã từng thực hiện giao dịch trong hệ thống.")
else:
    print(f"⚠️ User '{check_user}' chưa từng mua hàng.")

print("\n" + "=" * 65)
print(f"{'HOÀN THÀNH XỬ LÝ DỮ LIỆU':^65}")
print("=" * 65)
