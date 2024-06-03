def func(char):
    return f"{char} is a Alphabet" if char.isalpha() else f"{char} is not an Alphabet"

var = str(input())
print(func(var))
