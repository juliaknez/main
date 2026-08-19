#Prints whether prime number was entered
def isPrime(num):
    numbers = []
    for i in range(2, num+1):
        numbers.append(i)
    
    for i in numbers:
        j = 2
        if i>1:
            while j<len(numbers):
                if numbers[j]!=i:
                    if numbers[j]%i==0:
                        numbers.remove(numbers[j])
                j+=1

    return(numbers)


userInput=int(input("Please enter a number greater than or equal to 100: "))

print(isPrime(userInput))



