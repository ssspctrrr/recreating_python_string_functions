# get string_input
string_input = input("Enter string: ")

# get prefix
prefix = input("Enter prefix to be removed: ")

# check if prefix is at the start of string_input
if prefix == string_input[0:len(prefix)]:
    # slice string input if true
    string_input = string_input[len(prefix):]

# print result
print(string_input)