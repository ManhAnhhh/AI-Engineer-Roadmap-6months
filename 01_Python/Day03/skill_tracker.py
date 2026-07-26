# Chương trình quản lý danh sách kỹ năng bạn đang học.
skills = []

# Nhập danh sách kỹ năng
print("Nhập 5 kỹ năng bạn đang học:")
for i in range(5):
    skill = input(f"Kỹ năng {i+1}:")
    skills.append(skill)

# Hiển thị danh sách kỹ năng
print("\nDanh sách kỹ năng của bạn:")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")

# Xóa kỹ năng khỏi danh sách
skill_removed = input('Nhập skill muốn xóa: ')

if skill_removed in skills:
    skills.remove(skill_removed)
    print(f"Đã xóa kỹ năng {skill_removed} khỏi danh sách.")
else:
    print(f"Kỹ năng {skill_removed} không tồn tại trong danh sách.")

# Hiển thị lại danh sách kỹ năng sau khi xóa
print("\nDanh sách kỹ năng sau khi xóa:")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")

# Sắp xếp danh sách kỹ năng theo thứ tự alpha A -> B
skills.sort()
print("\nDanh sách kỹ năng sau khi sắp xếp (A -> B):")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")

doing = input('Bạn có muốn thêm kỹ năng mới không?  (y/n)').lower()
if doing == 'y':
    skill_added = input('Nhập kỹ năng muốn thêm: ')
    skills.append(skill_added)
    print(f"Đã thêm kỹ năng {skill_added} vào danh sách.")
else:
    print("Đã kết thúc chương trình.")

print('Tổng số skills: ', len(skills))

skill_searched = input('Nhập skill muốn tìm: ')

if skill_searched in skills:
    print(f'Bạn đang học {skill_searched}')
else:
    print(f'Bạn chưa học {skill_searched}')
    
