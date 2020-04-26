# Import ทั้งหมดทุกฟังก์ชั่นใน Module
# import numbers
# print(numbers.factorial(5))

# Import มาบางฟังก์ชั่น
# from numbers import factorial
# print(factorial(5))

# Import ทุกชังก์ชั่น
# from numbers import *
# print(factorial(5))
# print(fibonacci(100))

# Import และเปลี่ยนชื่อฟังก์ชั่น (Alias)
from numbers import factorial as fac, fibonacci as fib
print(fac(5))
print(fib(100))
