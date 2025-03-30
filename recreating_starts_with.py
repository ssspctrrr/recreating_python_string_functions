# get string_input
string_input = input("Enter string to be checked: ")

# get prefix
prefix = input("Enter prefix to find and check: ")

# check if prefix is start of string_input
if prefix == string_input[:len(prefix)]:
    # print "True. string_input starts with prefix."
    print(f'TRUE. "{string_input}" starts with "{prefix}".')
# else
else:
    # print "False. string_input does not start with prefix"
    print(f'FALSE. "{string_input} starts with "{prefix}".')