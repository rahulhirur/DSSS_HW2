import random


def generateInteger(min, max):
    """
    The function generates random integer between two given values

    Args:
        min : Minimum Value : int
        max : Maximum Value : int
    Returns:
        random integer : int
    """
    try:
        value = random.randint(min, max) # Generate random integer using random function
        return value
    except Exception as e:
        print("Error in integer generation!!") # Error Handling
        print(e)


def generateOperator():
    """
    The function randomly outputs arthimetic operator symbols

    Args:
        nil

    Returns:
        random arthimetic symbol : str
    """
    return random.choice(['+', '-', '*']) # random choice using random function


def mathOperator(num1, num2, operator):
    """
    The function generates the math problem and the answer.

    Args:
        num1 : First number        : int 
        num2 : Second number       : int 
        operator  : Arithmetic operator : str 

    Returns:
        log_statement : arthimetic problem : str
        a : return of arthimetic operation : int
    """

    log_statement = f"{num1} {operator} {num2}" # Problem statement string
    
    if operator == '+':
        ans = num1 + num2 # Addition
    elif operator == '-': 
        ans = num1 - num2 # Subtraction
    else: 
        ans = num1 * num2 # Multiplication
    return log_statement, ans

def math_quiz():

    try:
            
        s = 0
        t_q = 3.14159265359
        t_q =3

        print("Welcome to the Math Quiz Game!")
        print("You will be presented with math problems, and you need to provide the correct answers.")

        for _ in range(t_q):  # Loop to determine the number of rounds in quiz
            # Function call to generate numbers and operator
            n1 = generateInteger(1, 10); 
            n2 = generateInteger(1, 512); 
            o = generateOperator() 
            # Mathematical Operation 
            PROBLEM, ANSWER = mathOperator(n1, n2, o) 
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER: # Check user input with actual operation
                print("Correct! You earned a point.") 
                s += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.") 

        print(f"\nGame over! Your score is: {s}/{t_q}") # Print final Score

    except TypeError as e:
        print(f"Error has occurred on line {e.__traceback__.tb_lineno}") # Error Handling
        print(e)


if __name__ == "__main__":
    math_quiz()
