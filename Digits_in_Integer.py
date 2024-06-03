def digits(n):
    return len(str(n))  # args: n (int) : Integer to count the digits, returns the value

var = int(input())
count = digits(var)
print(count)