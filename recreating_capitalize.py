# get string_input
string_input = input("Enter string to be capitalized: ")

# assign result as uppercase of the first character of string_input
result = string_input[0].upper()

# check if length of string_input is greater than 1
if len(string_input) > 1:
    # concatenate result and lowercase of the 2nd to the ending characters of string_input
    result += string_input[1:].lower()

# print result
print(result)