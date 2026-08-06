# ============================================================
# Day06 - main.py  |  AI Engineer Roadmap
# Demo code - Hàm (Functions) trong Python
# ============================================================

print("--- 1. Định nghĩa hàm và gọi hàm ---")
def say_hello():
    print("Hello AI Engineer!")

say_hello()

print("\n--- 2. Tham số và Đối số ---")
def greet(name, message):
    print(f"Chào {name}, {message}")

greet("Mạnh Anh", "chúc bạn một ngày làm việc hiệu quả!") # Positional args
greet(message="bạn đang học AI à?", name="Thùy Linh")     # Keyword args

print("\n--- 3. Giá trị mặc định (Default arguments) ---")
def power(base, exponent=2):
    return base ** exponent

print("3 bình phương:", power(3))
print("3 mũ 3:", power(3, 3))

print("\n--- 4. Trả về nhiều giá trị (Return multiple values) ---")
def get_user_info():
    name = "Ngô Mạnh Anh"
    role = "AI Engineer"
    level = "Senior"
    return name, role, level  # Trả về dưới dạng Tuple

n, r, l = get_user_info()
print(f"User: {n}, Role: {r}, Level: {l}")

print("\n--- 5. *args (Nhận nhiều tham số không tên - Gom thành Tuple) ---")
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum 1:", calculate_sum(1, 2, 3))
print("Sum 2:", calculate_sum(10, 20, 30, 40, 50))

print("\n--- 6. **kwargs (Nhận nhiều tham số có tên - Gom thành Dictionary) ---")
def print_employee_details(**kwargs):
    for key, value in kwargs.items():
        print(f"- {key.capitalize()}: {value}")

print_employee_details(name="Nguyễn Linh Anh", age=24, department="AI Research", skills=["NLP", "Python"])

print("\n--- 7. Lambda Function (Hàm ẩn danh) ---")
square = lambda x: x ** 2
print("Lambda square 5:", square(5))

# Kết hợp lambda với filter, map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Số chẵn (filter + lambda):", evens)

squares_list = list(map(lambda x: x ** 2, numbers))
print("Bình phương các số (map + lambda):", squares_list)
