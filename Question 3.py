def eligibility(age):
    return age >= 18

def main():
    age = int(input("Input your age: "))
        
    if age > 18:
            print("You are eligible.")
    elif eligibility(age):
            print("You are eligible")
    else:
            print("You are not eligible")

if __name__ == "__main__":
    main()


age = int(input("Enter your age"))
 
if age >= 6 and age <= 18:
    print("Remain in school")
if age >=16:
    print("You are eligible to drive!")
    if age >= 18:
        print("You can vote and/or join the military!")
    if age >= 21:
        print("You can drink alcohol too.")
    if age >= 65 and age <=70:
        print("You are eligible to retire!")
    if age > 70 and age <=112:
        print("How did you live so long?")
else:
    print("Invalid age was entered.")



#A python program  that takes students mark as input and returns corresponding grade 
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80<90):
    print("Grade: B")
elif(avg>=70<80):
    print("Grade: C")
elif(avg>=60<70):
    print("Grade: D")
else:
    print("Grade: F")

#A program where the output is Invalid input
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80<90):
    print("Grade: B")
elif(avg>=70<80):
    print("Grade: C")
elif(avg>=60<70):
    print("Grade: D")
else:
    print("invalid Input!")


#A function to provide message along with the grade
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print(f"Grade: A; Excellent")
elif(avg>=80<90):
    print("Grade: B, Excellent")
elif(avg>=70<80):
    print("Grade: C, Good")
elif(avg>=60<70):
    print("Grade: D, satsifactory")
else:
    print("Grade: F, Needs Improvement")



















print("Enter Marks Obtained in 5 Subjects: ")
total1 = 44
total2 = 67
total3 = 76
total4 = 99
total5 = 58
 
total = total1 + total2 + total3 + total4 + total4
avg = total / 5
 
if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")