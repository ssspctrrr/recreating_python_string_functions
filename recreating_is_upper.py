# get string_input
string_input = input("Enter string to be checked if uppercased: ")

# define is_uppercase as False
is_uppercase = False

# iterate over the characters of string_input
    # get ascii_code of character
    # check if current character is not alphabetical
        # continue to next iteration
    # else if ascii_code is in range of 65 to 90 and character is alphabetical
        # set is_uppercase as True
    # else if ascii_code is not in range of 65 to 90 and character is alphabetical
        # set is_uppercase as False
        # break loop
# else:
    # if is_uppercase is True
        # print "string is uppercased"
    # else
        # print "string is not uppercased"