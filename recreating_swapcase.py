# get string_input
string_input = input("Enter string to reverse its casing: ")

# define result variable
result = ""

# iterate over the characters in string_input
for index in range(len(string_input)):
    # check if the current character is lowercased
    if string_input[index].islower():
        # assign swap_character as the uppercase of current character
        swap_character = string_input[index].upper()
        # concatenate swap_character to result
        result += swap_character
    # check if current character is uppercased
    elif string_input[index].isupper():
        # assign swap_character as the lowercase of current character
        swap_character = string_input[index].lower()
        # concatenate swap_character to result
        result += swap_character
    # else
    else:
        result += string_input[index]
        # concatenate current character to result

# print result
print(result)