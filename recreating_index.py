# get string_input
string_input = input("Enter string to be checked: ")

# get string_to_find
string_to_find = input("Enter character/s to find: ")

# iterate over index of string_input in lengths of string_to_find
for index in range(0, len(string_input)):
    # if current character/s == string_to_find
    if string_input[index:index + len(string_to_find)] == string_to_find:
        # print current index
        print(index)
        # break loop
        break
# else
else:
    # raise ValueError with message "substring not found"
    raise ValueError("substring not found")