# get string_input
string_input = input("Enter string to be checked: ")

# get string_to_find
string_to_find = input("Enter character/s to find: ")

print(string_input)
print(string_to_find)

# iterate over index of string_input in lengths of string_to_find
    # if current character/s == string_to_find
        # print current index
        # break loop
# else
    # raise ValueError with message "substring not found"