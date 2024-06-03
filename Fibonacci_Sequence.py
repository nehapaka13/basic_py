def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b # This line updates the current and next numbers in the sequence. The next number b becomes the current number a,
                        #    and the current number a becomes the sum of the current and next numbers.
    print()

var = int(input())
print(fibo(var))
