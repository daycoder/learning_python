"""
Built in python statement 'input' lets you get
values from the user from the console
"""

# Use it to pause execution

def main():
    input('Script stops here until you hit return >')

    string = input('Enter some string, and I\'ll print it 10 times >')

    # use _ to indicate we don't care about the value from range
    # we just want to do something 10 times
    for _ in range(10):
        print(string)

    # Print "Hello World!", as many times as the user wants
    iterations = input("How many Hello Worlds! ?")
    # use _ to indicate we don't care about the value from range
    # we just want to do something 10 times
    for _ in range(int(iterations)): # <-- works for good input, ValueError for non-integer
        print("Hello World!")


    # Print "Hello World!", as many times as the user wants
    iterations = input("How many Hello Worlds! ?")
    try:
        iterations = int(iterations)
    except ValueError as ve:
        #  Raise a new value error with more information
        raise ValueError(f'{iterations=} is not a valid integer ')

    # use _ to indicate we don't care about the value from range
    # we just want to do something 10 times
    for _ in range(iterations): # <-- works for good input, ValueError for non-integer
        print("Hello World!")

    # Function to safely get an integer from the user/console
    # : str is a type hint to say the parameter is *expected* to be a string
    # -> int is a type hint to say the functions is *expected* to return an integer
    def get_int_from_user(message: str) -> int:
        while True:
           hopefully_int = input(message)
           try:
               return int(hopefully_int)
           except ValueError:
               print(f'Sorry, {hopefully_int} isn\'t an integer. Please try again.')

    iterations = get_int_from_user('How many Hello Worlds! ?')
    # use _ to indicate we don't care about the value from range
    # we just want to do something 10 times
    for _ in range(iterations):  # <-- works for good input, ValueError for non-integer
        print("Hello World!")


    print('end!')

main()
