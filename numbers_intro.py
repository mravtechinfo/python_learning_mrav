#Numbers can be stored in variable

pi=3.14

print(pi)

#we can do math with numbers as we all know lol !

a=10
b=20

print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a**b)

# if you combine strings with numbers, Python gets confused

days_in_february = 28
#print(days_in_february + 'days_in_february')
# above line will give an error unsupported operand type(s) for +: 'int' and 'str' like this


#we actually typeacsted our number as string so that we can add to a string and print it.
#or pass it in string str function we can say that also
print(str(days_in_february) + 'days_in_february')


#Numbers can be stored as string  and treated as strings

#first_num='5'
#second_num='4'

#print(first_num+second_num)


#Number stored as strings must be converted to numeric values before dooing math

first_num = input('Enter first number ')
second_num = input( 'Enter second number ')

#Type casting is done here in int and float
print(int(first_num) + int (second_num) )
print(float(first_num) + float (second_num))

print(first_num+second_num)


