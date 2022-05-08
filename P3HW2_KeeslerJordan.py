#Calculate Pizza price using if and else statements
#CTI-110 P3HW2 Pizza Order
#Jordan Keesler
#8 MAY 2022
print('Please enter number of students.')
guest_num= int(input())

print('Please enter number of students sharing a pizza.')
guest_piz= float(input())

if guest_piz== 1.5:
    pizza_num=(guest_num/ guest_piz)
elif guest_piz== 2:
    pizza_num=(guest_num/ guest_piz)
elif guest_piz== 3:
    pizza_num=(guest_num/ guest_piz)
else:
     print('INVALID ENTRY!!!')
     print('Should have entered 1.5, 2, or 3')
     print('Run Program again')
     exit()
za_price= pizza_num*5
tax= za_price*.06
price= za_price+ tax
print('------Pizza Order------')
print('Number of Students:', format(guest_num,'.2f'))
print('Pizzas Needed:',format(pizza_num,'.2f'))
print('Price $',format(price,'.2f'))
print('-----------------------')
