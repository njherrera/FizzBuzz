# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def fizzBuzz(number):
    for x in range(1, number): # starting from 1, count up to the input number
        if x % 3 == 0 and x % 5 == 0: # if current number is divisible by 3 and 5, print FizzBuzz
            print("FizzBuzz")
        elif x % 3 == 0: # if current number is divisible only by 3, print Fizz
            print("Fizz")
        elif x % 5 == 0: # if current number is divisible only by 5, print Buzz
            print("Buzz")
        else: print(x)

if __name__ == '__main__':
    print_hi('PyCharm')
    fizzBuzz(20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
