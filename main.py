import random as r

# I am trying to generate the random numbers and numerators
def numberGen():
    number1 = r.randint(1,10)
    number2 = r.randint(1,10)
    # r.choice uses[] to define a list of string variables to pull from
    operator = r.choice(["+","-","*"])
    # concatanted to a single f string
    equation = (f"{number1} {operator} {number2} = ?")
    # print (equation) it prints

    # making string operators check int formula
    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    elif operator == "*":
        answer = number1 * number2
    # returning the equation and answer
    return equation, answer

# get user input
def userInput(answer):
    # looping
    while True:
        # try this code 
        try:        
            # if user enters anything other than a number it hits the except
            userInput = int(input("Enter your Answer: "))
            # if its the correct answer it breaks the loop and contiunues
            if (userInput) == answer:
                break
            # if incorrect print this message and break
            else:
                print(f"incorrect, the right answer is {answer}.")
                break
            # if not a number errors and loops to try again
        except ValueError:
            print("invalid input. please enter a whole number.")                


def main():
    # looping
    while True:
        # calls number gen and assigns the variables to it
        equation, answer = numberGen()
        # prints the equation
        print(equation)
        # calls user input
        userInput(answer)
        # if the user types anything except n it loops and recall the whole fuction to play again, i n it breaks and ends
        again = input("Press enter key to play again or 'n' to stop:").lower()
        if again == "n":
            break
main()