scores = {"james": 1828, "thomas": 3628, 'danny': 9310}
numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three'
}

print(scores)
print(numbers)

# เพิ่มสมาชิกใหม่เข้า Dictionay
scores['bobby'] = 4401
print(scores)

# การสร้าง Dictionary ว่าง
point = {}

# เพิ่มค่าเข้า Dictionary
point['Mr.A'] = 10.2
point['Mr.B'] = 15.4
point['Mr.C'] = 22.8
print(point)

# การ Loop อ่านสมาชิกของ Dictionary
for k in scores.keys():
    print(k)
for v in scores.values():
    print(v)
for k, v in scores.items():
    print(k, v)
