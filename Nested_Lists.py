"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

records=[["chi".20.0], ["betha".50.0],["alpha".50.0]]

The ordered list of scores is [20.0,50.0] , so the second lowest score is 50.0.
There are two students with that score:["betha","alpha"] . Ordered alphabetically, the names are printed as:

alpha
beta   

Input Format

The first line contains an integer,N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
2  ≤ N ≤ 5
There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry

"""


A=[]
B=[]
C=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    A.append([name,score])

for i in A:
    if i[1] not in C:
        C.append(i[1])
C=sorted(C)

A=sorted(A, key=lambda x: x[1])



low_score=C[1]
for estudiante in A:
    for score in estudiante:
        if score == low_score:
            B.append(estudiante[0])

B=sorted(B)
for names in B:
    print(names)     
