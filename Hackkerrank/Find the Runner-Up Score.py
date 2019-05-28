#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. 
#You are given scores. 
#Store them in a list and find the score of the runner-up.

#Input: first line containts n, second line contains an array A[]
#of n integers each seperated by a space.
n = int(input())
arr = list(map(int, input().split()))
second_arr =[]
for number in arr:
    if number != max(arr):
        second_arr.append(number)
print(max(second_arr))