# get string_input
string_input = input("Enter string to put in title-casing: ")

# define result
result = ""

# iterate over the indexes of the characters in string_input
for index in range(len(string_input)):
    # check if current index == 0 or previous character == " "
    if index == 0 or string_input[index - 1] == " ":
        # concatenate result and uppercase of current character
        result += string_input[index].upper()
    # else
    else:
        print(string_input[index])
        # concatenate the lowercase of current character

# print result
print(result)