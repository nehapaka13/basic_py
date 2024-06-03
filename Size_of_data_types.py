import sys

int = 12
float = 33.54
str = {"Hello"}
char = {'a', 'b'}
bool = True
list = [1, 2, 3]
tuple = (1, 2, 3)
dict = {"a" : 1, "b" : 2}
set = {1, 2, 3}


print(f"Size of Interger: {sys.getsizeof(int)} bytes")
print(f"Size of Float: {sys.getsizeof(float)} bytes")
print(f"Size of String: {sys.getsizeof(str)} bytes")
print(f"Size of Character: {sys.getsizeof(char)} bytes")
print(f"Size of Boolean: {sys.getsizeof(bool)} bytes")
print(f"Size of List: {sys.getsizeof(list)} bytes")
print(f"Size of Tuple: {sys.getsizeof(tuple)} bytes")
print(f"Size of Dictationary: {sys.getsizeof(dict)} bytes")
print(f"Size of Set: {sys.getsizeof(set)} bytes")
