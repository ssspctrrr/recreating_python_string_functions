# get string_input
string_input = input("Enter string to be lowercased: ")
print(string_input)

# iterate over the characters of string_input
for index in range(len(string_input)):

    # check if character is uppercased
    if string_input[index].isupper():
        print(string_input[index])
        # get ascii code of character
        # replace current character to its lowercase

# print string_input