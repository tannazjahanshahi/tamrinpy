Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=["tannaz","jahanshahi"]
>>> x.append("1378")
>>> print(x)
['tannaz', 'jahanshahi', '1378']
>>> x=[]
>>> a=input("enter your name: ")
enter your name: tannaz
>>> x.append(a)
>>> b=input("enter your lastname: ")
enter your lastname: jahanshahi
>>> x.append(b)
>>> c=input("enter your age: ")
enter your age: 21
>>> x.append(c)
>>> print(x)
['tannaz', 'jahanshahi', '21']
>>> print[2:]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print[2:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(x*2)
['tannaz', 'jahanshahi', '21', 'tannaz', 'jahanshahi', '21']
>>> print(x[2:])
['21']
>>> print(x[:2])
['tannaz', 'jahanshahi']
>>> print(x[0:1])
['tannaz']
>>> 