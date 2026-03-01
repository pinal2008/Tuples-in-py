# Topic :  [Tuples] 
 
#Syntax and Creation :
#Creating tuple
my_tuple = (10,20,30,40,50)
#Creating a tuple with different types of element
mixed_tuple = (10,"hello",3.14,(70,80,90))
#Creating a tuple without parentheses (optional but commonly used)
another_tuple = 1,2,3,4,5
#output : === Code Execution Successful ===
print(my_tuple) #output : (10, 20, 30, 40, 50)
print(mixed_tuple) #output : (10, 'hello', 3.14, (70, 80, 90))
print(another_tuple) # output : (1, 2, 3, 4, 5)


#single element tuple
single_element_tuple = (1,)

#Accessing Elements:
my_tuple = (10,20,30,40,50)
print(my_tuple[0]) #output : 10
print(my_tuple[2]) #output : 30
print(my_tuple[3]) #output : 40
print(my_tuple[4]) #output : 50
print(my_tuple[1]) #output : 20

#  [Tuple Methods:] 

# [1] count() : Returns the number of times a specified value appears in the tuple
my_tuple = (10,20,30,20,40,20)
print(my_tuple.count(2)) #output : 0

# [2] index(): Returns the index of the first occurrence of a specified value. Raises an errorif the value is not found 
my_tuple = (10,20,30,40,50)
print(my_tuple.index(30)) # output : 2


# [Tuple Operations :]

# [1] Concatenation : You can conacatenate two tuples using the + operator
tuple1 = [10,20,30]
tuple2 = [40,50,60]
combined_tuple = tuple1+tuple2
print(combined_tuple) #output : [10, 20, 30, 40, 50, 60]

# [2] Repetition : You can repeat a tuple using the * operator
my_tuple = (10,20,30)
repeated_tuple = my_tuple*3
print(repeated_tuple)  #output : (10, 20, 30, 10, 20, 30, 10, 20, 30)

# [3] Membership Test :you can check if an element exists in the tuple using the in keyword
my_tuple = (10,20,30,40)
print(30 in my_tuple) #output :True
print(50 in my_tuple) #output :False

# [4] Length : You can find the number of elemets in a tuple using the len() function 
my_tuple = (10,20,30,40,50,60)
print(len(my_tuple)) #output : 6

# [5] Slicing : you can extract a part of a tuple using slicing
#Example with a new tuple
my_tuple = (10,20,30,40,50,60)
print(my_tuple[2:5]) #output : (30, 40, 50)
print(my_tuple[:4])  #output : (10, 20, 30, 40)
print(my_tuple[3:])  #output : (40, 50, 60)

# Example : 2 Storing Multiple Values
# using a tuple to store multiple related values
person = ("yagnik",18,"Data Scientist")
name = person[0]
age = person[1]
profession = person[2]
print(f"Name:{name},Age:{age},Profession:{profession}")
# output : Name:yagnik,Age:18,Profession:Data Scientist


#Example 3: Unpacking a Tuple
# Unpacking tuple element into variables.
my_tuple = (1,2,3)
a,b,c = my_tuple

print("a",a) #output : a 1
print("b",b)  #output :b 2
print("c",c)  #output :c 3

#Example :4 Nested Tuples
# Creating a Tuple that contains other tuples
nested_tuple = (1,(2,3),(4,5,6))
#Accessing elements of nested tuples
print(nested_tuple[1])     #output :(2, 3)
print(nested_tuple[1][1])  #output :3
print(nested_tuple[2][0])  #output :4


















