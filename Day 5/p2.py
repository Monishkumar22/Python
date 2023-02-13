grade = input("Enter your grade: ")
salary=int(input("Enter the Employee salary:"))
if (salary<=0):
    bonus=0
    print("Enter the correct salary")
elif (grade=="A"):
    bonus=5/100*salary
    print(bonus)
    print(bonus+salary)
elif (grade=="B"):
    bonus=10/100*salary
    print(bonus)
    print(bonus+salary)    
elif (salary<=10000):
    bonus2=2/100*salary
    print(bonus2)
    print(bonus2+salary)
elif(salart<=0):
    print("Enter the correct salary")
else:
    print("Incorrect input")
