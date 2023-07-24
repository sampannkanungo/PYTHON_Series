#Function
def test():
    print("This is my very very first function")
test()

#2nd function
def test2():
    return "This is a 2nd statement"
print(test2())

#3rd function
def test3():
    return "Sampann",12,356.25,[1,2,3]
print(test3())

#assign the output in a,b,c,d
a,b,c,d=test3()
print(a)

#4th function
def test4():
    a=5-6/7
    return a
print(test4())

#5th function

def test5(a,b,c):

    d=a+b/c
    return d
print(test5(1,2,3))

#6th function
def test6(a,b):
    return a+b
print(test6(2,3))

#function using list : write a function , which extract the integer and float values in another list.

x=[1,2,3,4,"sam","k",[4,5,6,9,8]]
def list7(x):
    l1=[]
    for i in x:
        if type(i)==int or type(i)== float:
            l1.append(i)
    return l1
print(list7(x))



