

tamaño=int(input())
A=[]
B=[] 
entrada=""

for i in range(tamaño):
    entrada=input()
    entrada=entrada.split()
    entrada=[int(num) for num in entrada]         
    A.append(entrada)
    print(entrada)
    print(A)

print(A)
print(type(A[0][0]))
