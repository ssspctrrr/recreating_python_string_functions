# get string_input
string_input = input("Enter string to be checked: ")

# get string_to_count
string_to_count = input("Enter string to count: ")

# define index variable as 0
index = 0

# define count_of_string as 0
count_of_string = 0

# iterate while index < length of string_input:
while index < len(string_input):
    # check if string_to_count == ""
    if string_to_count == "":
        print("you are counting empty string")
        # assign count_of_string as length of string_input + 1
        # break loop 
    # else if string_input[index:index + length of string_to_count] == string_to_count
    if string_input[index:index + len(string_to_count)] == string_to_count:
        # increment count_of_string by 1
        count_of_string += 1
        # increment index by length of string_to_find
        index += len(string_to_count)
        # continue
        continue
    
    # increment index by 1
    index += 1

# print count_of_string
print(count_of_string)