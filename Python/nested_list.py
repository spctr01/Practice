'''
Given the names and grades for each student in a Physics class of students N, 
store them in a nested list and print the name(s) of any student(s) having the 
second lowest grade.

Input Format: 
The first line contains an integer,N,the number of students.
The 2N subsequent lines describe each student over 2lines; the first line 
contains a student's name, and the second line contains their grade. 
There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order
 their names alphabetically and print each name on a new line. '''
 
#####################################################################
if __name__ == '__main__':
    n = []
    s=[] 
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        n.append(name)
        n.append(score)
        s.append(list(n))
        n.clear()

    for x in s:
        if x[1] not in n:
            n.append(x[1])

    n.sort()

    for x in s:
        if n[1] == x[1]:
            names.append(x[0])

    names.sort()
    for a in names : print(a)

