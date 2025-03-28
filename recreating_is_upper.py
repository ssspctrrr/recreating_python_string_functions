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
        break

# if is_uppercase is True
if is_uppercase == True:
    # print "string is uppercased"
    print("TRUE. String is uppercased.")
# else
else:
    # print "string is not uppercased"
    print("FALSE. String is not uppercased.")