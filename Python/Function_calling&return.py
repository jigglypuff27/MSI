#Normal Function

# def fun1():
#     print('hello')

# fun1()            #Call a function hello is printed
# print(fun1())     #call a function hello is printed but function don't return anything so print returns none
# print(fun1)       #fun1 is an object whose address will be printed.


# def func2(arg1, arg2):
#     print(arg1," ",arg2)

# def func3(x):
#     return x*x*x

# print(func2(2,10)) #print and return none
# print(func3(3))    #func3 return 27 so that will be printed.



#Default value in the argument function

# def func4(var1, var2=1):
#     result = 1
#     for i in range(var2):
#         result=result*var1
#     return result

# print(func4(3))    #default value will be taken here by function has var2 value is not provided
# print(func4(3,7))  #normal function call 3topower7 is the output.

# print(func4(var2=5,var1=2))  #gives output 2 to the power 5 order not required with name and value is provided.

#Multi arguments in a function

def multiadd(*args):
    result=0
    for i in args:
        result=result+i
    return result

print(multiadd(2,3,4,5,1))  #gives output of addition of all numbers.
print(multiadd(1,2))        #same






    