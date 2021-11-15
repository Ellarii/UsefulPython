############### 2 ###############
def intcheck(question, low, high):

        error="Please enter an integer between {} and {}".format(low, high)
        value = "ValueError"
        while value == "ValueError":
            try:
                user_guess = int(input("Enter an integer between {} and {}:".format(low, high)))
                if low <= user_guess <= high:
                    value = ""
                    return user_guess
                else:
                    print(error)
                    print()
                    value = "ValueError"
            except ValueError:
                value = "ValueError"
                print (error)
                print ()
