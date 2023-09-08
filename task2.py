# Question # 02:

# Find the occurrence of the numbers in a Python list.
# List = [1, 2, 2, 3, 3, 3, 4, 5]
# Output_list = [1, 2, 3, 1, 1]

def find_occurances(list):
    # for storing each occurance I am using dictionary 
    each_value_counter = {}
    for number in list:
        if number in each_value_counter:
            # Look at the else condition for understanding
            each_value_counter[number] += 1
        else:
            # first visit to the element
            each_value_counter[number] = 1

    # PRINT HERE "each_value_counter" to check the concept

    # Now taking out uniques by list comprehension
    output = [each_value_counter[number] for number in each_value_counter.keys()] 
    return output



# UN-COMMENT THE BELOW CODE FOR GENERIC INPUT
# MAKE SURE AFTER UN-COMMENTING YOU COMMENT THE hard coded "input_list" BELOW 

# # "**************"
# input_list = str(input("Enter list comma seperated:"))
# input_list = input_list.split(",")
# # "**************"

input_list = [1, 2, 2, 3, 3, 3, 4, 5]

print(f'List: {input_list}')
print(f'Output_list: {find_occurances(input_list)}')