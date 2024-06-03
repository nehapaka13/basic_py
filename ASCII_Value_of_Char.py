def char_to_ascii(char):
    return ord(char)

character = str(input())
if len(character) == 1:
    ascii_value = char_to_ascii(character)
    print(f"The ASCII value of {character} is {ascii_value}")
