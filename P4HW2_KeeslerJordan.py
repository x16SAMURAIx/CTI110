# CTI-110
# P4HW2 - Pizza Order
# Jordan Keesler
# 9 APR 2022
#

nos =(("number of students you are ordering for? "))#nos = number of students
psp =(("how many students will be sharing each pizza? (1.5, 2, or 3)"))#psp = people sharing pizza

answer = 'y'
while answer == 'y':
    nos = float(input("number of students you are ordering for? "))#nos = number of students
    psp = float(input("how many students will be sharing each pizza? (1.5, 2, or 3)"))#psp = people sharing pizza
    pn = round(nos/psp + .5) #pizzas needed before rounding, adding .5 to garuntee it always rounds up
    pbt = (pn * 5) #price before tax
    tax = (pbt * 0.06) #sales tax assuming 6%
    pat = (pbt + tax) #price after tax
    if(psp == 1.5 or psp == 2 or psp == 3):
        print("----Pizza Order--------")
        print("Number of Students :",nos)
        print("Pizzas Needed :",pn)
        print("price $",pat)
        print("--------------------------")
        answer = input('would you like to run the program again (y for yes)')
        if answer == 'y':
            continue
    else:
        print("INVALID ENTRY!!!!")
        print("should have entered 1.5, 2, or 3")
        print("")#blank line
        float(input("Enter number of people per pizza again.(1.5, 2, or 3)"))
