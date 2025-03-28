# get total_characters
total_characters = int(input("Enter the number of total characters: "))

# get string_input
string_input = input("Enter string to be centered: ")

print(total_characters - len(string_input))

# check if string_input is greater than total_characters
if total_characters <= len(string_input):
    # pass
    print("no spaces needed")
# else if the spaces to be filled can be divided evenly by left and right
elif (total_characters - len(string_input)) % 2 == 0:
    print("even spaces in left and right")
    # assign spaces as total_characters - length of string_input
    # concatenate half the spaces in the left and right
# else if the spaces to be filled are not even in left and right
else:
    print("uneven spaces in left and right")
    # assign spaces as total_characters - length of string_input
    # assign left_spaces as rounded down spaces divided by 2
    # assign right_spaces as spaces - left spaces
    # concatenate the left_spaces and right_spaces to string_input

# print string_input