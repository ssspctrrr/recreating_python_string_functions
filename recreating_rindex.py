# get string_input
string_input = input("Enter string to be checked: ")

# get string_to_find
string_to_find = input("Enter character/s to find from the end: ")

print(string_input, string_to_find)

# iterate over reverese indexing of string_input in lengths of string_to_find
    # check if current character/s == string_to_find
        # print index
        # break loop
# else
    # raise ValueError with message "substring not found"