#Basic While Loop code:
a=1
while a <= 10:
     print(a)
     a=a+1

#from this above code, extract the output and show the sum .
result = 0
a=1
while a <=10:
     result=result+a
     a=a+1
print("sum of the output is {0}".format(result))

#Find out the factorial of given number : 1,2,3,4,5
number = int(input("Enter a number "))
factorial = 1
while number > 0:
     factorial=factorial*number
     number = number - 1
print("The factorial is {0}".format(factorial))

#Fibbonacci Series using while loop : 0,1,1,2,3,5....

n= int(input("Enter the number of your choice "))
a,b=0,1
s = 0
while s < n:
     print(a)
     c=a+b
     a=b
     b=c
     s=s+1

#reverse a string using while loop
s = input("Enter your string for reversal ")
reverse = ""
len=(len(s))
while len>0:
     reverse=reverse+s[len-1]
     len=len-1
print(reverse)

#Print multiplication table using while loop

n= int(input("Please enter your number "))
i=1
while i<=10:
     result=n*i
     print(n,"*",i,"=",result)
     i=i+1




