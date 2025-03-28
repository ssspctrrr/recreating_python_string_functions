# get total_characters
total_characters = int(input("Enter the number of total characters: "))

# get string_input
string_input = input("Enter string to be centered: ")

# check if string_input is greater than or equal to total_characters
if total_characters <= len(string_input):
    # pass
    pass
# else if the spaces to be filled can be divided evenly by left and right
elif (total_characters - len(string_input)) % 2 == 0:
    # assign spaces as total_characters - length of string_input
    spaces = total_characters - len(string_input)
    print(spaces)
    # concatenate half the spaces in the left and right
# else if the spaces to be filled are not even in left and right
else:
    # assign spaces as total_characters - length of string_input
    spaces = total_characters - len(string_input)
    print(spaces)
    # assign left_spaces as rounded down spaces divided by 2
    # assign right_spaces as spaces - left spaces
    # concatenate the left_spaces and right_spaces to string_input

# print string_input