#COMPREHENSION IN PYTHON PROGRAMMING
#Writing process : [return | statement | Condition]

#list comprehension
#QUESTION 1 : WRITE A CODE TO FIND THE SQUARE OF EACH NUMBER IN ARRAY
l=[1,2,3,4,5,6]
l1=[]
for i in l:
    l1.append(i**2)
print(l1)

### Write the above code in single line
p=[i**2 for i in l]
print(p)

#Write a single line code to find the number in output which is divisible by 2
r=[i for i in l if i%2==0]
print(r)

#convert the given list in upper case in a single line code
l2=["sam" , "sun" , "ras"]
u=[i.upper() for i in l2]
print(u)

#Dictionary comprehension
#find out the square of given dictionary
d={"key1":1,"key2":2,"key3":3}
x={k:v**2 for k,v in d.items()}
print(x)

