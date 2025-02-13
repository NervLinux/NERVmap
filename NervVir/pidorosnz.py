# z, x = map(int(input())
# print(z + x )

# pix = int(input())
#
# if pix < 0:
#     print(sum((range(1, pix - 1))))
# else:
#     print(sum((range(1, pix + 1))))

# 1	5
# 7	<
# 2	-7
# -12	>
# 3	13
# 13	=

# 5
# 7  <
# -7
# -12 >
#
# 12
# 12 =

z = int(input("Введи первое число: "))
x = int(input("Введи второе число: "))

if z > x: print(">")
elif z < x: print("<")
elif z == x: print("=")