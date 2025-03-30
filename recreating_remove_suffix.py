# get string_input
string_input = input("Enter string to remove suffix: ")

# get suffix
suffix = input("Enter suffix to remove: ")

# check if suffix == end of string_input
if suffix == string_input[-len(suffix):]:
    # slice string if true
    string_input = string_input[:-len(suffix)]

# print string_input
print(string_input)