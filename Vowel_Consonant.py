def check(char):
    char = char.lower()     #converting the character to lower case to handle both the Upper and Lower case
    vowels = {'a', 'e', 'i', 'o', 'u'}

    if char.isalpha():      #Check if the given character is alphabet
        if char in vowels:
            return f"{char} is a Vowel"
        else:
            return f"{char} is a Consonant"
    else:
        return f"{char} is not a valid alphabet"

var = str(input())      #Enter any Character you want to check
print(check(var))