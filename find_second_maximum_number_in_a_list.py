"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given  scores.
Store them in a list and find the score of the runner-up.

Input Format

The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Constraints

2 ≤ n ≤ 10
-100 ≤ A[i] ≤ 100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

"""

n=int(input())
A=list(map(int,input().split()))
   
max=-100
runnerup=-101
for num in A:
    if num >max:
        max=num
for num in A:        
    if num >-101 and num <max and num > runnerup:
        runnerup=num

print(max)
        
print(runnerup)