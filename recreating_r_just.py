# get total_characters
total_characters = int(input("Enter number of total characters: "))

# get string_input
string_input = input("Enter string to be right-justified: ")

# check if total_characters geater than length of string_input
if total_characters > len(string_input):
    # assign spaces as total_character - length of string_input
    spaces = total_characters - len(string_input)
    print(spaces)
    # concatenate spaces at start of string_input

# print string_input