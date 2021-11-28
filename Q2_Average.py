marks = [ 78, 89, 85, 91, 93, 82, 79 ]
sum=0
for i in range(0,len(marks)):
    sum = sum+marks[i]

Average = sum / len(marks)
print("Average of Marks "+str(Average))
