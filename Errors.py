#print(my_variable)
'''a=int(input('enter key'))
my_dict={1:10,2:20,3:30}
print(my_dict)
if a>3:
    raise KeyError('key not found')

#IndexError
my_list=[1,2,3]
print(my_list)
index=int(input('enter index'))
if index>=2:
    raise IndexError('index out of range')

#ImportError
try:
    raise ImportError("Custom import error message")
except ImportError as e:
    print(e)'''

#ArithmeticError
a=int(input('enter no:'))
b=int(input('enter no:'))

try:
    res=a/b
    raise ArithmeticError('Division by zero')
except ArithmeticError as ae :
    print(ae)
    