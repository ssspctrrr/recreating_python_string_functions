# get string_input
string_input = input("Enter string to be uppercased: ")

# define result as empty string
result = ""

# iterate over the characters of string_input
for character in string_input:
    # check if current character is lowercased
    if character.islower():
        # get ascii code of current character
        ascii_code = ord(character)
        print(ascii_code, character)
        # concatenate its uppercase to result
        result += character
    # else
    else:
        # concatenate current character to result
        result += character

# print result
print(result)