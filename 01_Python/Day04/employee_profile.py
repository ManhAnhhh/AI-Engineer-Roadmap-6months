# ============================================================
# Day04 - employee_profile.py
# Mini Project
# ============================================================

employee = (
    "Ngo Manh Anh",
    23,
    "AI Engineer",
)

print(f"Tên: {employee[0]}, Tuổi: {employee[1]}, Vị trí: {employee[2]}")

numbers = (1, 2, 3, 4, 5)
# 2 phần tử đầu
print(numbers[1:3])
# 2 phần tử cuối
print(numbers[-2:])
# Tuple đảo ngược
print(numbers[::-1])

# Dùng Unpacking để lấy:
name, age, job = employee
print(f"Name: {name}, Age: {age}, Job: {job}")

a = 10
b = 20
a, b = b,a

skills = [
    "Python",
    "SQL",
    "Python",
    "AI",
    "SQL",
    "Python"
]

unique_skills = set(skills)

# add
unique_skills.add("AI")
unique_skills.add("Git")
unique_skills.add("Docker")

# unique_skills.remove("Java") -> báo lỗi vì k có Java trong set
unique_skills.discard("Java") # -> xóa phần tử k quan tâm có tồn tại trong set không

backend = {"Python", "SQL", "API"}
ai = {"Python", "Machine Learning", "AI"}
#Intersection
inter = backend.intersection(ai)
#Diff
diff1 = backend.difference(ai)
diff2 = ai.difference(backend)

print('Tổng skills', len(skills))
print('Skills duy nhất', len(set(skills)))
# Các skill bị trùng chưa làm được


# AI Skill Gap Analyzer
my_skills = {
    "Python",
    "SQL",
    "Git",
    "Linux"
}
# Công việc AI Engineer yêu cầu:
required_skills = {
    "Python",
    "SQL",
    "Git",
    "Linux",
    "Machine Learning",
    "Deep Learning",
    "Numpy",
    "Pandas",
    "PyTorch",
    "Docker"
}
# in kỹ năng tôi có
print("Kỹ năng tôi có: ", my_skills)
# in kỹ năng cần thiết cho công việc AI Engineer
print("Kỹ năng cần có: ", required_skills)

# in kỹ năng còn thiếu (kỹ năng cần có nhưng tôi không có)
missing_skills = required_skills - my_skills
print("Kỹ năng còn thiếu: ", missing_skills)

# in kỹ năng thừa (kỹ năng tôi có nhưng không có trong required_skills)
excess_skills = my_skills - required_skills
print("Kỹ năng thừa: ", excess_skills)

# in kỹ năng chung (kỹ năng tôi có và có trong required_skills)
common_skills = my_skills.intersection(required_skills)
print("Kỹ năng chung: ", common_skills)

progress = len(my_skills & required_skills) / len(required_skills) * 100

print(f"Tiến độ học tập của bạn: {progress:.1f}%")
