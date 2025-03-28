# get string_input
string_input = input("Enter string to be checked if uppercased: ")

# define is_uppercase as False
is_uppercase = False

# iterate over the characters of string_input
for index in range(len(string_input)):
    # get ascii_code of character
    ascii_code = ord(string_input[index])
    
    # check if current character is not alphabetical
    if string_input[index].isalpha() == False:
        # continue to next iteration
        continue
    # else if ascii_code is in range of 65 to 90 and character is alphabetical
    elif ascii_code in range(65, 91):
        # set is_uppercase as True
        is_uppercase = True
    # else if ascii_code is not in range of 65 to 90 and character is alphabetical
    else:
        # set is_uppercase as False
        is_uppercase = False
        # break loop

    print(string_input[index], is_uppercase)

# else:
else:
    print("loop else triggered")
    # if is_uppercase is True
        # print "string is uppercased"
    # else
        # print "string is not uppercased"