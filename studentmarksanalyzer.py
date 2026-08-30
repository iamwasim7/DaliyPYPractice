#Student marks analyzer**
# Use - functions, loops, conditionals, and diffrent built-in methods/ functions.
#Take marks of 5 subjects and calculate:
#-  Total marks 
#-  Percentage 
#-  Highest mark 
#-  Lowest mark 
#-  Grade 



marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)


def calculation_result():
    total = sum(marks)
    percentage = total/5
    highest_mark = max(marks)
    lowest_mark = min(marks)
    
    if percentage >= 90:
        grade = "A+ Grade"
    elif percentage >= 80:
        grade = "A Grade"
    elif percentage >= 70:
        grade = "B Grade"
    elif percentage >= 60:
        grade = "C Grade"
    elif percentage >= 50:
        grade = "D Grade"
    else:
        grade = "F Grade"
    
    print("Total marks:", total)
    print("Percentage:", percentage, "%")
    print("Highest mark:", highest_mark)
    print("Lowest mark:", lowest_mark)
    print("Grade:", grade)


calculation_result()