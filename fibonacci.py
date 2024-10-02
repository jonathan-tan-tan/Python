""" 
    Serie Fibonacci
escribe un programa que escriba los 50 primeros numeros de la serie de Fibonacci empezando en 0.
la serie de Fibonacci se compone poruna sucesión de números en la que el siguiente es la suma de los dos anteriores.
0,1,1,2,3,5,8,13,21

"""

def fibonacci(n):
    serie=[0,1]
    if n<2:
        print(serie[n-1])
    else:
        for i in range (2,n):
            nuevo=serie[-1]+serie[-2]
            serie.append(nuevo)
    print(serie)        

"""

def fibonacci(n):
    fib_1=0
    fib_2=1
    if n <2:
        print(n-1)
    else:
        print(fib_1,fib_2,end=" ")
        for i in range (n-2):
            fib_sig= fib_1 + fib_2
            print(fib_sig, end=" ")
            fib_1=fib_2
            fib_2=fib_sig


"""            

fibonacci(50)

