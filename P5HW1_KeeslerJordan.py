#This function will drop the score of the lowest letter grade and get the average number and letter grade.
#29 APR 2022
#CTI-110 P5HW1 - Score list
#Jordan Keesler
#
def main():
    menu()
    
def menu():
    repeat = 1
    choice = 0
    grade_list = []
    while repeat != 0:
        print()
        print("----MENU----")
        print("1. Create Score List")
        print("2. Display Results")
        print("3. Exit")
        print("------------")


        choice = input("Enter a choice (1, 2 or 3): ")
        if choice == '1':
           grade_list = listofgrades()
        elif choice == '2':
            if len(grade_list) == 0:
                print('List not created!')
            else:
                calGrades(grade_list)
        elif choice == '3':
            repeat = 0
        else:
            print("Invalid Entry")
            print("Please Try again")
            repeat = 1

    print("Thank you for playing, but...")
    print("Program has been targeted for termination! Get to the chopper!")

def List(score):
    grade_list = []
    i = 0
    #Loop
    while i < score:
        grades = int(input(f'Enter score #{i + 1}: '))
        #Determines if score is less than zero or greater than 100
        if 0 > grades or grades > 100:
            print('Invalid Entry!\nEntry must be between 0 and 100!')
            i = i
        else:
            grade_list.append(grades)   
            i += 1
    return grade_list

def calGrades(grade_list):
    lowest = min(grade_list)
    grade_list.remove(lowest)
    average = sum(grade_list) / len(grade_list)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    BlipBloop = [lowest, grade_list, average, grade]
    disGrades(BlipBloop)

def listofgrades():
     total = int(input("Enter number of grades to total: "))
     grade_list = List(total)
     return grade_list

def disGrades(Display):
    print()
    print('Lowest score:',Display[0])
    print('List of scores (lowest omitted):',Display[1])
    print('Average:',Display[2])
    print('Letter Grade:',Display[3])
main()
