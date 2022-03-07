#Input from User
print('Prime Average Detection from Given Range!');

testNumber = int(input('Please Enter First Range Value: '))
testNumber2 = int(input('Please Enter Last Range Value: '))

#Init Array
primeNumbers = []

for num in range(testNumber, testNumber2 + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
            else:
                print(num, end='\t')
                primeNumbers.append(num)                 
                break

#For average
avg = sum(primeNumbers) / len(primeNumbers)
print('\n\nAverage is :'+ str(avg) )
                
               

