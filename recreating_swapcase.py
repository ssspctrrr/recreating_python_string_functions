# get string_input
string_input = input("Enter string to reverse its casing: ")

# iterate over the characters in string_input
for character in string_input:
    # check if the current character is lowercased
    if character.islower():
        print(character, "lower")
        # convert current character to its uppercase
    # check if current character is uppercased
    elif character.isupper():
        print(character, "upper")
        # convert current character to its lowercase

# print string_input