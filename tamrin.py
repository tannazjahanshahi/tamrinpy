# def maxnum(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# x=12
# y=23
# z=33
# a=maxnum(x,y)
# b=maxnum(a,z)
# print(b)

# def sum(numbers):
#     s=0
#     for i in numbers:
#         s+=i
#     return s
# print(sum((10,20,30)))

# def string_reverse(str1):
#     s=''
#     i=len(str1)
#     while i>0:
#         s+=str1[i-1]
#         i=i-1
#     return s
# print(string_reverse("tannaz"))  
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))
# ----
# def testrange(x):
#     if x in range(3,9):
#         print("in range")
#     else:
#         print("not in range")

# testrang(10)
# ----
# def dastan(s):
#     u=0
#     l=0
#     for i in s:
#         if i.isupper():
#             u+=1
#         elif i.islower():
#             l+=1
#         else:
#             pass
#     return u,l
# print(dastan("TANNAZ tannaz"))
# def foo(n):
#     if n==1:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if (n % i==0):
#                 return False
#         return True

# print(foo(7))

# def foo(VORODI):
#     DATA=[]
#     for Yeki in VORODI:
#         if Yeki %2== 0:
#             DATA.append(Yeki)
#     return DATA

# print(foo([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# def TABE(VORODI_TABE):
#     HAFEZE=0
#     for YEKI_AZ_MAGHADIR in range(1,VORODI_TABE):
#         if VORODI_TABE % YEKI_AZ_MAGHADIR == 0:
#             HAFEZE+=YEKI_AZ_MAGHADIR
    
#     return VORODI_TABE==HAFEZE

# for i in range(0,9000):
#     if TABE(i): 
# #         print(i)
# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('aza')) 
    