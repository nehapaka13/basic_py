def func(num):
    return f"{num} is even" if num % 2 == 0 else f"{num} is odd"

num = int(input())
print(func(num))