#code 1
def multiply (a, b):
    return a*b
print(multiply(3,4))
#code 2
counter = 0
for i in range(4):
    counter = counter + 1
    print(counter)
#code 3
age = int(input("Enter your age:"))
if age >= 18:
    print("adult")
#code 4
a = 3
b = 4
temp = a
a = b = temp
print(a)
print(b)