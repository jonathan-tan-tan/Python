"""
Task

You are given two arrays A and B. Both have dimensions of NxN.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.

Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]


"""


tamano=int(input())
A=[]
B=[] 
entrada=""

for i in range(tamano):
    entrada=input()
    entrada=entrada.split()
    entrada=[int(num) for num in entrada]         
    A.append(entrada)

for i in range(tamano):
    entrada=input()
    entrada=entrada.split()
    entrada=[int(num) for num in entrada]         
    B.append(entrada)
    
import numpy 

print(numpy.dot(A,B))
