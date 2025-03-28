# get number of total_characters
total_characters = int(input("Enter the number of total characters: "))

# get string_input
string_input = input("Enter string to be left-justified: ")

# check if total_characters is greater than string_input
if total_characters > len(string_input):
    # get the number of spaces to fill
    spaces = total_characters - len(string_input)
    print(spaces)
    # concatenate the spaces to string_input

# print string_input