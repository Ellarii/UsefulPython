############### 1 ###############
def checkinput(input_string, comparison_list=["", "", ""]): # comparison list compares itself to the user input
    continue_function_check = True #tells the loop to continue
    while continue_function_check == True:
            input_string = input("Please select one of the options\nEither _, _ or _\n")
            input_string = input_string.lower() # .lower means the input gets switched to lowercase, making it easier to compare
            if input_string in comparison_list: # if input is in the list:
                continue_function_check = False # Stop the function after this if: function finishes
                return input_string # Make the original variable with the function in it, have the input value
            else: 
                continue_function_check = True
    # Optimisation Suggestions provided by 19285#6430 on Discord
