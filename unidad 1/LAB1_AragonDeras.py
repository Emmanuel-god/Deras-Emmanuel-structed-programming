#code A
grades = [80 ,90, 70]
average = sum(grades)/ len(grades)
print (average)
#code B
def calculate_average(data):
    return sum(data) / len(data)
grades = [80, 90, 70]
print(calculate_average(grades))
#code C
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x:x**2, numbers))
print(squares)
#code C(mod)
numbers = [23, 15, 18, 32, 8]
squares = list(map(lambda x:x**2, numbers))
print(squares)