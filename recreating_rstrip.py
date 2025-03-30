# get string_input
string_input = input("Enter string (preferably with several spaces at the end): ")

# check if length of string_input is more than 1
if len(string_input) > 1:
    # iterate over the reverse indexing of string_input
    for index in range(len(string_input) - 1, -1, -1):
        print(index, string_input[index])
        # check if current character is not " "
        if string_input[index] != " ":
            # split string_input from start to current character
            # break loop
            print("split here")
            break

# print string_input
print(f'RESULT: "{string_input}"')