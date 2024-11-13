gradelist=[]
passed=[]
failed=[]
while len(gradelist)!=5:
    grade=float(input("Input Student Grade: "))
    if grade<=100 and grade>=40:
        gradelist.append(grade)
        if grade>=75:
            passed.append(grade)
        else:
            failed.append(grade)
    else:
        print("Invalid Grade Input!(Must be 40-100)")
        break
if len(gradelist)==5:
    gradetotal=gradelist[0]+gradelist[1]+gradelist[2]+gradelist[3]+gradelist[4]
    average=gradetotal/5
    passpoint=len(passed)/5
    passpercent=passpoint*100
    print(f"Percentage of Students Passed: {passpercent}%")
    print(f"Average of Student Grades: {average}")
    print(f"Inputted Grades: {gradelist}")
    print(f"Number of Students Who Passed: {len(passed)}")
    