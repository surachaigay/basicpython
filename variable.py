a = 3
b = 4.92
c = "itgenius"

print(a)
print(b)
print(c)

# การสร้างตัวแปรหลายตัวในบรรทัดเดียวกัน
x = y = z = 10
print(x, y, z)

j, k = 5, 15
print(j, k)

status = True
msg = False
print(status, msg)

# ตัวแปรแสดงผลร่วมกับข้อความ
# วิธีที่ 1 Concat String
print("ราคาขายต่อชิ้น ", b, " บาท")

# วิธีที่ 2 String Interpolation
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3 Format String
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
