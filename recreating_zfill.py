# get number of total_characters
total_characters = int(input("Enter number of characters: "))

# get string_input
string_input = input("Enter string to be added with zeroes: ")

# define is_signed as True

# check if length of string_input is greater than or equal to total_characters
if len(string_input) >= total_characters:
    # pass
    pass
# else
else:
    # assign zeroes as total_character - length of string_input
    zeroes = total_characters - len(string_input)

    # check if string is signed
    if string_input[0] in ["+", "-"]:
        # concatenate the sign, zeroes, to string_input
        string_input = string_input[0] + "0" * zeroes + string_input[1:]
    # else
    else:
        # concatenate zeros to string_input
        string_input = "0" * zeroes + string_input

# print string_input
print(string_input)