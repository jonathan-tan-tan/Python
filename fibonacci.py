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

fibonacci(50)


