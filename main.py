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
    fizzBuzz(20)


