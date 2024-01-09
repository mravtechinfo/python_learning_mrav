# List is a collection of items
# List are always mutable menaing you can change them

from array import array # We have to create an array object to use array 
# We are just importing an array from array library to use it in simple words we can say that.
# Arrays code are from line number 26
names=['Anubhav', 'Aditya', 'Amit','Vaibhav']
scores=[]
scores.append(200)
scores.append(190)
scores.append(300)
scores.insert(0,10)
print(scores)

print(names)

print(scores[1])
print(names[0])






# Array is also a collection of items
marks = array('d') # this is an array object where d is double type array to be made is specified

marks.append(91.2)
marks.append(33.33)
marks.append(44.2)
print(marks)

print(marks[1])


# Array - 
# Store numerical data types.
# All the elements msut of similar type or same type .

# List -
# Store anything of any type.


# Common Operations on Lists

print(len(names)) # len gives total number of elements in the list or length of list
scores.insert(3,48) # can store at a particular index 
print(names)
print(scores)
names.sort() # do sorting .
scores.sort()
print(names)
print(scores)


presenters =  names[0:2] # here [0:2] 0-inlcuded and 2- not included in the range
print(presenters)

# Dictionary 

# When we have  to sue things with key value pairs (key,value) lile this.