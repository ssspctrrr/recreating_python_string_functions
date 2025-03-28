# get string_input
string_input = input("Enter string to be checked: ")

# get suffix
suffix = input("Enter suffix to be located at the end of string: ")

# check if suffix is at the end of string_input
if string_input[-len(suffix):] == suffix:
    # print True
    print(f"TRUE. {string_input} ends with {suffix}.")
# else
else:
    # print False
    print(f"FALSE. {string_input} does not end with {suffix}.")