# def max(z,k):
#     if z>k:
#         return z
#     else:
#         return k
# a=56
# b=255
# c=98
# z=max(a,b)
# k=max(z,c)
# print(max(z,k))


# def sum_list(vorodi):
#     l=0
#     for i in vorodi:
#         l+=i
#     return l
# print(sum_list((45,56,1)))



# def sum_list(vorodi):
#     l=0
#     for i in vorodi:
#         l+=i
#     print (l)
# sum_list((45,56,1))



# def average(x,y,z):
#     sum=x+y+z
#     a=sum/3
#     return a
# print(average(4,5,6))



# def multipy(numbers):
#     n=1
#     for i in numbers:
#         n*=i
#     return n
# print(multipy((1,5,8,6,3)))



# def reverse(he):
#     str=""
#     c=len(he)
#     while c>0:
#         str+=he[c-1]
#         c-=1
#     return str
# print(reverse("123lkj"))


# 10
# def even(vorodi):
#     s=[]
#     for i in vorodi:
#         if i%2==0:
#             s.append(i)
#     return s
# print(even([1,2,4,3,7,9]))



# Exercise Question 1: Create a function that can accept two arguments name and age and print its value
# def sth(name,age):
#     print(name,age)
# sth("tannaz",21)


# Exercise Question 2: Write a function func1() such that it can accept a variable length of  argument and print all arguments value
# def fun(*v):
#     for i in v:
#         print(i)

# fun(20, 40, 60)
# fun(80, 100)

# def fun(z):
#     for i in range(z,120,z):
#         print(i)
# fun(20)

# Exercise Question 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
# def calculation(m,n):
#     return m+n , m-n
# print(calculation(10,23))


# Exercise Question 4: Generate a Python list of all the even numbers between 4 to 30
# def even(num):
#     s=[]
#     for i in num:
#         s.append(i)
#     return s
# print(even((4,32,2)))



# Make a Python function that takes x as argument and returns y. Call the function for x=2 and print the answer.(y=6x2+3x+2,x=2)
# def f(x):
#     return 6*x**2+3*x+2
# y=f(2)
# print(y)


# Write a function x(n) for computing an element in the sequence xn=n2+1. Call the function for n=4 and write out the result.
# def x(n):
#     return n**2+1
# xn=x(4)
# print(xn)


# First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".
# def shut_down(s):
#     if s=="yes":
#         print("shutting down") 
#     elif s=="no":
#         print("Shutdown aborted")
#     else:
#         print("sry")
# s="yes"
# shut_down(s)



# First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".
# def distance_from_zero(foo):
#     if type(foo)== int or type(foo)==float:
#         return abs(foo)
#     else:
#         return "nope"
# print(distance_from_zero((-5.9)))
# print(distance_from_zero("what?"))

# myfunc = lambda a : a * 10
# print(myfunc(2))
# a = "Hello, World!"
# print(a.replace("saeed", "Bye"))

# a = "Hel lo, Wor ld!"
# print(a.split(" "))

# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" in txt
# print(x)

# age = 30
# age2 = 36
# txt = "My name is %d John, and I am %d " %(age,age2)
# print(txt)

# myfile=open("test.txt","r")
# myfile.close()
# m=open("test.txt","r")
# print(m.read(5))
# print(m.read(10))
# print(m.read())
# print("\nend")
# print(m.read())
# m.close()


# file=open("test.txt","r")
# print(file.readlines())
# file.close()


# """nbcjnnx
# bjcjnknmckm
# mnmnk k"""



# file=open("test.txt","r")
# for line in file:
#     print(line)
# file.close()



# file=open("test.txt","w")
# file.write("hello this is a text")
# file.close()
# file=open("test.txt","r")
# print(file.read())
# file.close()


# try:
#     file=open("test.txt")
#     print(file.read())
# finally:
#     file.close()

# with open ("test.txt") as file:
#     print(file.read())





# jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
# jobj_list =   '["Red", "Green", "Black"]'
# jobj_string = '"Python Json"'
# jobj_int = '1234'
# jobj_float =  '21.34'

# import json as js
# c=js.loads(jobj_string)
# x=c.replace("Python","saeed")
# f=open("test.txt","w")
# f.write(x)
# f.close()

# with open("testu.txt","r", encoding="UTF-8") as f:
#     print(f.read())

#function >> with open >> vorodish dict >>
# import json
# def  jsread():
#     with open("test.txt","r") as f:
#         return json.load(f)

# def  xoo(foo):
#     with open("test.txt","w") as f:
#         json.dump(foo,f)
# dic={"name":"tannaz","family":"jahanshahi"}

# xoo(dic)
# print(jsread())
 