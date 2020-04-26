# การสร้างข้อมูลแบบ List
number = [5, 8, 13, 24, 7, 16]
name = ["John", "Jane", "jany", "Wasan"]
mixed = [10, 25.75, True, 'Samit']

# การเข้าถึงสมาชิกใน List
print(number[1])
print(name[3])
print(mixed[2], mixed[3])

# การนับจำนวนสมาชิกใน List
print("สมาชิกทั้งหมดของ number =", len(number))

# การสร้าง List แบบว่าง (Empty List)
data = []

# การเพิ่มสมาชิกเข้าไปใน List ว่าง
data.append(10)
data.append(15)
data.append(20)
print(data)

# การอัพเดทสมาชิกใน List
data[1] = 12
print(data)

# ฟังก์ชั่นวนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print(n)

# Loop แล้วหาผลรวม
sum = 0
for n in number:
    sum += n
print(sum)
