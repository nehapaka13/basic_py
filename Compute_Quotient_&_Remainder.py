a = int(input())    # a being the divident; Example:17
b = int(input())    # b being the divisor; Example: 5
q = a // b          # logically in math, we get the quotient where q = [a / b]
r = a - b * q       # and reminder is as simple as in maths
print(q)
print(r)