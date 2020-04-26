# การสร้างฟังก์ชันแบบไม่มีการ Return Value
def hello(name='Surachai P.'):
    print(f"Hello {name}")

# สร้างฟังก์ชันแบบมีการ Return Value


def area(width, height):
    total = width * height
    return total


# เรียกใช้งานฟังก์ชัน hello()
hello("Gay")
hello()

# เรียกใช้งานฟังก์ชัน area()
print(area(30, 50))
print(area(15, 7.5))
