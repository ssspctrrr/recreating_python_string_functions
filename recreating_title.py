# get string_input
string_input = input("Enter string to put in title-casing: ")

# define result
result = ""

# iterate over the indexes of the characters in string_input
for index in range(len(string_input)):
    print(index, string_input[index])
    # check if current index == 0 or previous character == " "
        # concatenate result and uppercase of current character
    # else
        # concatenate the lowercase of current character

# print result