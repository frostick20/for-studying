n = int(input()) 

num1 = int(input())
num2 = int(input())

if num1 > num2:
    max1 = num1
    max2 = num2
else:
    max1 = num2
    max2 = num1

for _ in range(n - 2):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)