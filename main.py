# math_utils.py

def add_numbers(a, b):

    return a + b

def multiply_numbers(a, b):

    return a * b

def greet_user(name):

    return f"Hello, {name}! Welcome to VS Code."

def main():

    print(add_numbers(10, 15))

    print(multiply_numbers(4, 5))

    print(greet_user("Rain Stewart"))

if __name__ == "__main__":

    main()


    # a. Syntax Highlighting 
    # - Uses unique colors for code elements
    # - Different colors for functions, variables, strings (purple, green, orange, etc)
    # - Helps us to easily recognize different parts of code, better readability and mistake identification

    # b. Code Completion
    # - Automatically suggests matches for functions or variables or other elements while typing
    # - Similar to mobile autocorrect if that can be counted as an analogy
    # - Reduces typing effort, speeds up coding, lesser spelling mistakes
    # - Prevents errors during function calling by suggesting existing/correct names and parameters

    # c. Debugging Tools
    # - Breakpoints pause programs before executing the line on that breakpoint
    # - Lets you see what happens in the program, thus making it easier to understand the thought process
    # - Shows you where errors occur and helps you identify bugs easily

    # d. Error Detection
    # - VS detects the syntax error by underlining the code with red squigglies
    # - Shows an error indicator, hovering over redlined code will let VS explain the error
    # - E.g; "(" was not closed