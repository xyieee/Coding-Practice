# Integer N is the number of students. Next input records student's name 
# and their percent marks in three subjects. Marks can be floating values.
# Save the record in a dictinary data type. 
# Output: The average of the marks obtained by the particular student.
# Correct the output to 2 decimal places. 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score=student_marks[query_name]
    print('%.2f' %(sum(query_score)/len(query_score)))