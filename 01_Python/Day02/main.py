# join: chuyển từ mảng sang chuỗi
a = ['a1', 'b', 'c']
c = 'aa a a'
b = ','.join(a)
# print(b)

# text[start:end]
# start được lấy, end không được lấy.

# split
r = 'a,b,c,d,e,f'
# print(r.split(','))

# format :
salary = 20000000

# print(f'Salary: {salary:<,.2f} VND')

text = "AI Engineer"
# print(text.replace(' ', '\n'))

a = text.split()
# print(','.join(a))

# print(text.split())

# Reverse string
t = 'hnil'
if t == t[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

g = 'Python,JavaScript,C#,SQL'

print(g.replace(',', '\n'))





