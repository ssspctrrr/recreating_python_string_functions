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
        print(swap_character)
        # concatenate swap_character to result
    # check if current character is uppercased
    elif string_input[index].isupper():
        # assign swap_character as the lowercase of current character
        swap_character = string_input[index].lower()
        print(swap_character)
        # concatenate swap_character to result
    # else
    else:
        print(string_input[index])
        # concatenate current character to result

# print string_input