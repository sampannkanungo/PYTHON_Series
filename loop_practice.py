l1=["sam" , "sun" , "mam",1,2,3]
#above there is a list given

#Separate them into a integer list and string list
l=[]
l2=[]
for i in l1:
    if type(i)==int or type(i)==float:
        l.append(i)

    else:
        l2.append(i)

print(l)
print(l2)

#next problem : if some ones value is SUN in the list ; prints its previous values.
for i in l1:
    if i=="sun":
        break
    print("The answer of 2nd question is " + i)

#3rd Problem :
l3=[]
for i in l1:
    if i== "sun":
        continue
    l3.append(i)
print(l3)

#range function : reverse the list using range function
l5=[]
for i in range(len(l1)-1,-1,-1):
    l5.append(l1[i])
print(l5)

# Given a new List: Print the number present in the even list
l4=[23,5,45,56,6,67,78,87,8998,9,9,8]
l6=[]
for i in range(0,len(l4),2):
    l6.append(l4[i])
print(l6)

# Given a list : Find the sum of the list
l7=[1,2,3,4,5,6,7,8,98]
result = 0
for i in l7:
    result= result+i
print(result)

#These are the small and basis for loop practice question


