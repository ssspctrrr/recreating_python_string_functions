# get string_input
string_input = input("Enter string (preferably with several spaces at the start): ")

# iterate over the indexes in_string input
for index in range(0, len(string_input)):
    # check if the indexed character is not a space
    if string_input[index] != " ":
        # slice string_input at the current index if true
        string_input = string_input[index:]
        # end loop
        break

# print result
print(f'RESULT: "{string_input}"')