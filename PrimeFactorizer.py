#Get input num
InputNum = int(input("What is your number?\n"))

#Init some lists we use later, and a mutable copy of InputNum
PrimeNums = []
ModNum = InputNum
PrimeFacts = []

#The next loop gets us a handy list of prime numbers up to the user input number
print("The prime numbers up to " + str(InputNum) + " are...")
print("(for numbers over ~30,000 this can take some time to compute!)")
for num in range(2,InputNum + 1):
    #Status helper, to let you know how much has been processed for large requests
   if num % 1000 == 0:
       print("Just processed "+ str(num))
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           PrimeNums.append(num)

print("The primes up to " + str(InputNum))
print(str(PrimeNums) + "\n")

while ModNum > 1:
    if InputNum in PrimeNums:
        print("That is a prime number you nerd!")
        PrimeFacts = [ModNum]
        break
    for i in PrimeNums:
        if ModNum % i == 0:
            PrimeFacts.append(i)
            ModNum = ModNum / i

print("The prime factorization of " + str(InputNum) + " is...\n" + str(PrimeFacts))
