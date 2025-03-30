# get string_input
string_input = input("Enter string to be uppercased: ")

# define result as empty string
result = ""

# iterate over the characters of string_input
for character in string_input:
    # check if current character is lowercased
    if character.islower():
        print(character, "convert to uppercase")
        # get ascii code of current character
        # concatenate its uppercase to result
    # else
    else:
        print(character, "stay")
        # concatenate current character to result

# print result