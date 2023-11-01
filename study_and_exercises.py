persons = ["Francesco","Davide","Federico","Riccardo","Giuseppe","Simone"]

#list
print(type(persons))

print(persons)

print(len(persons))

print(persons[0])

for name in persons :
    print("Il nome " + name + " e' formato da " + str(len(name)) + " lettere.")
    for letter in name :
        print(letter)


#tuple
x = ("apple", "banana", "cherry")
print(type(x))



#dict dictionary
x = {"name" : "John", "age" : 36}
print(type(x))


#bool
x = True
print(type(x))


#casting
x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)
print(x)



#len
x = "Hello World"
print(len(x))


#first letter
txt = "Hello World"
x = txt[0]


#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)



#Return the string without any whitespace at the beginning or the end.
txt3 = " Hello World "
print(txt3)
x = txt3.strip()
print(x)



#Convert the value of txt to upper case.
txtHello = "Hello World"
txtHello = txtHello.upper()
print(txtHello)



#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
print(txt)



#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)



#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am  {}"
print(txt.format(age))



#The statement below would print a Boolean value, which one? TRUE
print(10 > 9)



#The statement below would print a Boolean value, which one?  FALSE
print(10 == 9)



#The statement below would print a Boolean value, which one?  FALSE
print(10 < 9)



#The statement below would print a Boolean value, which one?  TRUE
print(bool("abc"))



#The statement below would print a Boolean value, which one?  FALSE
print(bool(0))



#Multiply 10 with 5, and print the result.
print(10 * 5)



#Divide 10 by 2, and print the result.
print(10 / 2)




#Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
    
    


#Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
    print("5 and 10 is not equal")
    
    

#Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")
    
    
    
"""
LIST  LIST  LIST  LIST  LIST 
"""
    
    

#Print the second item in the fruits list.1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])




#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits[0] = "kiwi"
print(fruits)



#Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)



#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.insert(1, "lemon")
print(fruits)



#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.remove("banana")
print(fruits)



#Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])



#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])



"""
TUPLE  TUPLE  TUPLE  TUPLE  TUPLE
"""


#Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))



#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])



#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))


#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])


#Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])



"""
SET   SET   SET   SET   SET
"""

#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")



#Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  #add aggiunge "orange" e gestisce l'indice dell'elemento randomicamente!
print(fruits)



#Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) #update aggiunge la list dentro set e gestisce gli indici degli elementi randomicamente! 
print(fruits)



#Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)



#Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

  
  

"""
DICTIONARY  DICTIONARY  DICTIONARY  DICTIONARY
"""

#Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))



#Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car["year"] = 2020
print(car)




#Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"  #ultimo item!
print(car)



#Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)



#Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)






#IF .. ELSE

#Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b :
    print("Hello World")
    
    
#Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b :
    print("Hello World")
    
    
    
#Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b :
    print("Yes")
else:
    print("No")
    
    
    
#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b :
    print("1")
elif a > b :
    print("2")
else:
    print("3")
    
    
    
#Print "Hello" if a is equal to b, and c is equal to d.
a = 50
b = 10
c = 50
d = 50
if a == b and c == d :
    print("Hello")
else:
    print("Not eguals!")
    
    
    
    
#Print "Hello" if a is equal to b, or if c is equal to d.
a = 50
b = 10
c = 50
d = 50
if a == b or c == d:
    print("Hello")
    
    
    
#This example misses indentations to be correct. Insert the missing indentation to make the code correct:
if 5 > 2:
    print("Five is greater than two!")
    
    
    
#Use the correct short hand syntax to put the following statement on one line:
if 6 > 2 : print("Six is greater than two!")



#Use the correct short hand syntax to write the following conditional expression in one line:
print("Yes") if 5 > 2 else print("No")



#WHILE    WHILE    WHILE


#Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1
print("6 non e' minore di 6 (6 < 6) pertanto esce dal ciclo!")




#Stop the loop if i is 3.
i = 1
while i < 6:
    if i == 3:
        break  #i==3 ? allora esci dal ciclo!
    print(i)
    i += 1



#In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
      continue #i==3? allora saltalo ma vai avanti ciclando altro!
  print(i)




#Print a message once the condition is false.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i non e' minore di 6")





#FOR LOOPS   FOR LOOPS   FOR LOOPS


#Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
    
    
#In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["kiwi", "ananas", "strawberry"]
for x in fruits:
  if x == "ananas":
      continue
  print(x)
  
  

#Use the range function to loop through a code set 6 times.
for x in range(6) :
    print(x)
    
    
    
    
#Exit the loop when x is "banana".

people = ["Federico", "Francesco", "Davide"]
for name in people:
  if name == "Francesco":
      break
  print(name)
  
  
  

#FUNCTIONS   FUNCTIONS     FUNCTIONS

#Create a function named my_function.
def my_function() :
    print("Hello from a function")

my_function()



#Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
  print(fname, lname)

my_function("Francesco","Rapisarda")



#Let the function return the x parameter + 5.
def my_function(x):
  return x + 5
print(x)




#If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])
    
    
    
    
#If you do not know the number of keyword arguments that will be passed into your function, 
#there is a prefix you can add in the function definition, which prefix?


def my_function(**kid):
  print("His last name is " + kid["lname"])
  
  
  
  

#CLASSES    CLASSES    CLASSES


#Create a class named MyClass:
class MyClass :
    x = 5
    
    
    
    
#Create an object of MyClass called p1:
class MyClass:
    x = 5
    p1 = MyClass()
    print(p1.x)