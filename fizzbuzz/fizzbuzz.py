def fizzbuzz(number):
    x = ""
    if number % 3 == 0 and number % 5 == 0:
        x = x + "fizzbuzz"
    elif number % 3 == 0:
        x = x + "fizz"
    elif number % 5 == 0:
        x = x + "buzz"
    return x
