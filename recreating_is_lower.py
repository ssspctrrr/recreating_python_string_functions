# get string_input
string_input = input("Enter string to check if lowercased: ")

# define is_lower as False
is_lower = False

# iterate over the characters of string_input
for character in string_input:
    print(character)
    # get ascii_code of current character

    # check if current character is alphabetical
        # continue to next iteration
    # else if ascii_code is in range of 97 to 122
        # set is_lower as True
    # else
        # set is_lower as False
        # break loop

# check if is_lower == True
    # print "String is lowercased"
# else
    # print "String is not lowercased"