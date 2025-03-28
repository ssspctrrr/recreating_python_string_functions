# get string_input
string_input = input("Enter string to be lowercased: ")

# define result variable
result = ""

# iterate over the characters of string_input
for index in range(len(string_input)):

    # check if character is uppercased
    if string_input[index].isupper():
        # get ascii code of character
        ascii_upper = ord(string_input[index])
        print(ascii_upper, string_input[index])
        # concatenate the lowercase to result
        result += string_input[index]
    # else if character is not uppercased:
    else:
        # concatenate current character to result
        result += string_input[index]

# print result
print(result)