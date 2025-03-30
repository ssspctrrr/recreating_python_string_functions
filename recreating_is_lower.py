# get string_input
string_input = input("Enter string to check if lowercased: ")

# define is_lower as False
is_lower = False

# iterate over the characters of string_input
for character in string_input:
    # get ascii_code of current character
    ascii_code = ord(character)

    # check if current character is not alphabetical
    if character.isalpha() == False:
        # continue to next iteration
        continue
    # else if ascii_code is in range of 97 to 122
    elif ord(character) in range(97, 123):
        # set is_lower as True
        is_lower = True
    # else
    else:
        # set is_lower as False
        is_lower = False
        # break loop
    print(character, is_lower)

# check if is_lower == True
    # print "String is lowercased"
# else
    # print "String is not lowercased"