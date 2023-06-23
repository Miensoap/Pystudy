def print_hello(n):    
    if n == 0:        
        return        

    print_hello(n - 1) 
    print('HelloWorld')    


print_hello(int(input()))
