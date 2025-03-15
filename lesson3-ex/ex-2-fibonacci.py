def fibonacci(n):
    first = 0
    second = 1

    for i in range(int(n)):
        print(str(first) + ' ')
        first_temp = first
        first = second
        second = first_temp + second
        
 
print('Enter nth fibonacci number you want to see: ')
fib_n_th = input()
print('Your fibonacci serie is: ')
fibonacci(fib_n_th)