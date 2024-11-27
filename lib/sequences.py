def print_fibonacci(length):
    
    fibonacci = [0, 1]  

   
    for i in range(2, length):
        next_number = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(next_number)


    print(fibonacci[:length])


print_fibonacci(9)  
