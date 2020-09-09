# # for i in range(6):
# #     for j in range(i):
# #         print ('* ', end="")
# #     print('')
# # for i in range(6,0,-1):
# #     for j in range(i):
# #         print('* ', end="")
# #     print('')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Declaring the tuple
# cnt_odd=0
# odd_list=[]
# cnt_even=0
# even_list=[]

# for i in numbers:
#     if i%2==0:
#         cnt_even+=1
#         even_list.append(i)
#     else:
#         cnt_odd+=1
#         odd_list.append(i)

# print(f'odd numbers are {odd_list} and count is : {cnt_odd }')
# print(f'even numbers are {even_list} and count is : {cnt_even }')

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
# x=0 #false
# y=1 #true
# if not(0):
#     print("yes")

# def Fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     # First Fibonacci number is 0 
#     elif n==1: 
#         return 0
#     # Second Fibonacci number is 1 
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2) 
  
# # Driver Program 
  
# print(Fibonacci(25)) 
  