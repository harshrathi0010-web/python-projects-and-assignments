# loops and pattern printing assignments

#ques. print number use a loop from 1-10

##for i in range(1,11):
##    print(i)

#ques. print even number between 1 and 20

##for i in range (1,21):
##    if i%2==0:
##        print(i)

#ques. find sum of numbers from 1-10
##sum=0
##for i in range(1,11):
##    sum+=i
##print("sum is:",sum,end=" ")

#ques..Take a number from the user and print its multiplication table up to 10.

##num=int(input("Enter the num:"))
##for i in range(1,11):
##    print(num*i)

#ques.Take a string and count the total number of characters using a for loop.

##str=input("enter the string:")
##count=0
##for ch in str:
##    count+=1
##print("total character:",count)

# Break Related Questions

#ques.Print numbers from 1 to 10 Stop the loop when the number becomes 5.

##for i in range(1,11):
##    print(i)
##    if i==5:
##        break

#ques.Search for number 25 in a list If found, print "Found" and stop the loop.
##numbers=[25,10,30,5,34]
##for num in numbers:
##    if num==25:
##        print("found",num)
##        break


#ques.Given a list of numbers print the first negative number and stop the loop.

##numbers=[25,-10,30,5,34]
##for num in numbers:
##    if num<0:
##        print("found:",num)
##        break

#       Continue Related Questions 

#ques. Print numbers from 1 to 10 Skip number 5.

##for i in range(1,11):
##    if i==5:
##        continue
##    print(i)

#ques.Print numbers from 1 to 20 Skip all even numbers.
##for i in range(1,21):
##    if i%2==0:
##        continue
##    print(i)

#ques.Print each character of the string "PYTHON" Skip the letter "O".

##word="PYTHON"
##for ch in word:
##    if ch=="O":
##        continue
##    print(ch)

#     Pass Related Questions 

#ques.Run a loop from 1 to 5 but do nothing inside the loop using pass.

##for i in range(1,6):
##    pass

#ques. Loop from 1 to 10 If number is 6, just use pass.
##
##for i in range
##(1,11):
##    if i==6:
##        pass
##else:
##    print(i)

#ques.Q14. Search Number Using for-else Search for number 100 in a list. If found, print "Found".
#If not found, print "Not Found".


#.Take a number from the user and check whether it is prime using for-else.

##num=int(input("enter the num:"))
##if num<=1:
##    print("not prime number")
##else:
##    for i in range(2,num+1):
##        if num%i==0:
##            print("not prime number")
##            break
##    else:
##        print(" prime number")


#  Pattern Questions

##*
##* *
##* * *
##* * * *
##* * * * *

##for i in range(1,6):
##    for j in range(1,i+1):
##        print("* ",end="")
##    print()

##* * * * *
##* * * *
##* * *
##* *
##*

##for i in range(5,0,-1):
##    for j in range(1,i+1):
##        print("* ",end="")
##    print()

##1 
##12 
##123 
##1234 
##12345

##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    print()

##    *
##   * *
##  * * *
## * * * *
##* * * * *

##for i in range(1,6):
##    for k in range(5,i,-1):
##        print(" ",end="")
##        
##    for j in range(1,i+1):
##        print("* ",end="")
##    print()

#Print a star pattern Stop printing when the row number reaches 4.

##for i in range(1,6):
##  if i==4:
##      break
##    
##  for j in range(i):
##        print("*",end="")
##  print()


             #while loop
#ques.Print numbers from 1 to 10 using a while loop.

##i=0
##while i<10:
##    i+=1
##    print(i,end="  ")

#ques.Print even numbers from 1 to 20.

##i=0
##while i<=20:
##    i+=2
##    print(i)

#ques. Print odd numbers from 1 to 20.

##i=1
##while i<20:
##    print(i)
##    i+=2


#ques.Print numbers from 10 to 1 (reverse order).

##i=10
##while i>=1:
##    print(i)
##    i-=1

#ques.Print multiplication table of 5 using while loop.

##i=0
##while i<10:
##    i+=1
##    print(5*i)


                  # Intermediate Level

#ques.Find the sum of first 10 natural numbers using while loop.

##i=1
##sum=0
##while i<=10:
##    sum+=i
##    i+=1
##    
##print("sum is:",sum)

#ques.Find factorial of a number entered by user.

##num=int(input("enter the number:"))
##i=1
##fact=1
##while i<=num:
##    fact*=i
##    i+=1
##print(fact)

#ques.Count number of digits in a given number.

##n=int(input("enter the number:"))
##count=0
##while n>0:
##    n=n//10
##    count+=1
##print(count)

#Check whether a number is palindrome or not using while loop.

#





            

    
    
    
    
        
        





    











    
    
    





