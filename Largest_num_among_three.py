def find_largest(a, b, c):
    return a if a > b and a > c else b if b > c else c

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(f"The largest Among {num1}, {num2}, {num3} is {find_largest(num1, num2, num3)}")