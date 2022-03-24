housevalue = float(input('Type the value of the house: '))
salary = float(input('Type your salary: '))
years = int(input('Type How many years do you want to pay the installment: '))
print('=>'*30)
installment = housevalue / (years * 12)
print('Your monthly installment cost {:.2f}'.format(installment))
print('=>'*30)
thirdofsalary = salary * 30/100
print('30 % of your salary cost {:.2f}'.format(thirdofsalary))
print('=>'*30)

if installment <= thirdofsalary:
    print('Congrats baby, you got the house !!!')
else:
    print('Sorry baby, work hard to ear more money')
