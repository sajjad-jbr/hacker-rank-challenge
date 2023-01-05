def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][0] > sub_li[j + 1][0]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li

def findMin(studentList):
    min1 = studentList[0]
    min2 = [studentList[1]]
    for i in range(1,len(studentList)):
        s = studentList[i]
        if min1[1]!=s[1]:
            min2 = [s]
            break
    
    temp = []
    tempMin1 = []

    if min1[1] > min2[0][1]:
        temp = min1
        min1 = min2[0]
        min2[0] = temp

    for student in studentList:
        tempMin1 = min1
        if min1[1] > student[1]:
            min1 = student
        if student[1] < min2[0][1] and student[1] > min1[1]:
            min2 = [student]
        elif min2[0][1] == student[1] and min2[0][0] != student[0]:
            min2.append(student)
    min2 = Sort(min2)
    for m in min2:
        print(m[0])

if __name__ == '__main__':
    studentList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])
    findMin(studentList)
