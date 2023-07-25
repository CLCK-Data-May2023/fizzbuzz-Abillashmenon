# add your code here
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FIZZBUZZ")
    elif n % 5 ==0:
        print('Buzz')
    elif n % 3 ==0:
        print('Fizz')
    else:
        print('This number is not applicable with FIZZBUZZ - ', n)

