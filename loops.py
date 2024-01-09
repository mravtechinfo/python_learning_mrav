# Loop - doing a same task again and again
# Loops through a collection 

for name in ['Anubhav','Vaibhav','Amit', 'Abhishek','Achintya','Twinkle','Aditya']:
    print(name)

# Looping a number of times 

for index  in range (0,10): # Here also 10 is not included in the range
    print(index)

names = ['Anubhav','Vaibhav','Amit', 'Abhishek','Achintya','Twinkle','Aditya']

index = 0

while index < len(names):
    print(names[index])
    # Change the condition!!
    index = index + 1