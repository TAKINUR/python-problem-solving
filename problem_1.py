##Prime Time


#Input from User
testNumber = int(input('Please Enter Test Number: '))

#Validate Number
if testNumber < 1 or testNumber > 10000:
    testNumber = int(input(' Please Enter positive Number Between 1 and 10000: '))
    

for i in range(2, testNumber):
    if testNumber % i != 0:
        newNumber = testNumber * 5 + 3
        print('The Result of Prime Value: ' + str(newNumber))
        break
    else:
        newNumber = testNumber // 2
        print('The Result is ' + str(newNumber))
        break

