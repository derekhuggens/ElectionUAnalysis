from typing import ItemsView


print("Hello World")

type(3)

type(73.81)

type("Hello World")

type("")

type(True)

#Creating Variables

num_candidates = 3
wining_percentage = 73.81
candidate = "Diane"
won_election = True

#Order or Operations

5 + 2 * 3
8 // 5 - 3
8 + 22 * 2 - 4
16 - 3 / 2 + 7 - 1
3 ** 3 % 5
5 + 9 * 3 / 2 - 4
(5 + 2) * 3
(8 // 5) - 3
8 + (22 * (2 - 4))
16 - 3 / (2 + 7) - 1
3 ** (3 % 5)

5 + (9 * 3 / 2 - 4)
(9 * 3 / (2 - 4))

#Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures
#lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists #lists 

counties = ["Arapahoe","Denver","Jefferson"]
counties[0]
counties[2]
print(counties[2])
print(counties[-1])

#Length of a List

len(counties)

#Slicing a list
#Format is: list[start : end], end is not included, but start is.

#To find the frist and second items in the list
counties[0:2]

#Only retrieves the first item on the list
counties[0:1]

#Short hand to get first and second items but not the last, third item
counties[:2]

#Conversely, this format gets the second and third items
counties[1:]

#Adding items to a list
### Use append() function in the syntax: list.append()

counties.append("El Paso")
counties

### To append into a list at a certain location use syntax: list.insert(index, obj)

counties.insert(2, "El Paso")
counties

### To remove an instance from a list use syntax: list.remove("obj")
counties.remove("El Paso")
counties.remove("El Paso")
counties.remove("El Paso")
counties

### Another remove method is pop() to remove at a certain index
counties.pop(3)

### Change an element in a list, use syntax: list[index] = NEWVALUE
counties[2] = "El Paso"
counties

counties.pop(2)
counties.append("Jefferson")
counties.insert(2, "El Paso")
counties.remove("Arapahoe")
counties.insert(2, "Denver")
counties.remove("Jefferson")
counties.insert(1, "Jefferson")
counties.append("Arapahoe")
counties.remove("Denver")

#Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures
#tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples #tuples 

# immutable
### create a tuple using syntax: my_tuple = ( ) or you can use my_tuple = tuple()

my_tuple = ()
my_tuple = tuple()

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
type(counties_tuple)

counties_tuple[1]


#Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures #Data structures
#Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries #Dictionaries 

# word = key, definition = value
# {"python" : "constricting_snake"}

# syntax is {key:value}

# more than one element or key-value pair is separated by commas.

#     {key1:value1, key2:value2}

# There are two key rules for dictionaries:
#
# Values in a dictionary can be objects of any type: integers, floating-point decimals, strings, Boolean values, datetime values, and lists.
# Keys must be immutable objects, like integers, floating-point decimals, or strings. Keys cannot be lists or any other type of mutable object.

### To initilize or create a dictionary use the syntax: my_dictionary = {}    or      the dict() method as,      my_dictionary = dict()

counties_dict = {}
type(counties_dict)

#  The standard format for creating a key in a dictionary is to place the key between single or double quotes and inside brackets.

counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict

len(counties_dict)

counties_dict.items()
# items inside the dict_items([]) is known as a VIEW OBJECT

### To get all the keys of a dictionary add the keys() method at the end.

counties_dict.keys()

### To get all the values from a dictionary, add the values() method at the end.

counties_dict.values()

### To get a specific value from a dictionary in two methods. Use the get() method

counties_dict.get("Denver")

# How would you get the number of registered voters in Arapahoe county? All of the below

# counties_dict['Arapahoe'] 

# counties_dict.get("Arapahoe")  

# print(counties_dict['Arapahoe'])  

# print(counties_dict.get("Arapahoe")) 

### Another method to get a specific value from a dictionary is this format:     dictionary_name[key], the key must be in single or double quotes or you will get NameError.

counties_dict["Arapahoe"]


### Lists of Dictionaries:     [{key1:value1, key2:value2}, {key1:value3, key2:value4}]

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data

# Above, the keys are county and registered_voters. To compare to Excel, the keys are columns and the values are the values in Excel rows.


### Decision Statements

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

## example

# if condition:
#   statement 1
#   statement 2

# ie      if len(counties) > 2

# whitespace matters in Python, indentation must be consistent for interpreter to determine beginning and end of code block.

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


### if-else statements: also knowns as a dual-alternative decision statement.

# General format

# if condition:
   #statement 1
   #statement 2
# else:
   #statement 1
   #statement 2


### Nested if-else statments
### Nested ie-elif-else statements

# See examples in Election_analysis folder

### Membership Operators:    in    &   not in

# in

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


# not in

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" not in counties:
    print("True") 
else: 
    print("False")

### Logical Operators:    and      or     not


# and

x = 5
y = 5
if x == 5 and y == 5:
    print("True") 
else:
    print("False")

# or

x = 5
y = 5
if x == 3 or y == 5:
    print("True")
else:
    print("False")


# not

x = 5
y = 5
if not(x > y):
    print("True") 
else:
    print("False")

# Combining Membership and Logical operations

# in with and

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# in with or

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")



### Repetition Statements, also known as Loops.    While Loops,  For Loops

# Condition-Controlled loop is known as a While Loop
# Count-Controlled loop is known as a For loop.

# while loop

x = 0
while x <= 5:
    print(x)
    x = x + 1

# for loop

# for item in [items]:
#    statement 1
#    statement 2

for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

# simpler version is to use the range() function instead of for

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])


### Recreate the count_dict

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# .keys() will iterate through the counties_dict dictionary and print out the keys.


for county in counties_dict.keys():
    print(counties)

# .values will iterate through the counties_dict dictionary and print out the values.

for voters in counties_dict.values():
    print(voters)

# can also do it this way

for county in counties_dict:
    print(counties_dict[county])

# use the items() method to iterate through the counties_dict dictionary and print out the key-value pair.

for key, value in counties_dict.items():
    print(key, value)

# or as such

for key, value in counties_dict.items():
    print(county, voters)

# First variable declared in the for loop is assigned to the keys, the second variable is assigned to the values.

for key, value in counties_dict.items():
    print(county, "county has", voters, "registered voters.")


### Skill Drill

counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for i in range(len(counties)):
    for voters in counties_dict.values():
        print(counties[i], "county has", voters, "registered voters.")

### Iterating through a list of dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

########

for i in range(len(voting_data)):
    print(voting_data[i])

### Getting the Values from a List of Dictionaries

## First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. Then, in the second for loop, use the values() method on the variable county_dict to reference the data in the second for loop in order to get each value.

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

## How would you retrieve the number of registered voters from each dictionary?

for county_dict in voting_data:
    print(county_dict['registered_voters'])

## How to print out only the county name from each dictionary?

for county_dict in voting_data:
    print(county_dict['county'])


### Printing Formats


## print() function ## print() function ## print() function ## print() function ## print() function ## print() function ## print() function ## print() function ## print() function ## print() function ## print() function 



## F-Strings: Formatted String Literals ## F-Strings: Formatted String Literals ## F-Strings: Formatted String Literals ## F-Strings: Formatted String Literals ## F-Strings: Formatted String Literals ## F-Strings: Formatted String Literals

# Original

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# F-String format

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


###### Using F-Strings with Dictionaries


# Original code with concatenation

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# Now with F-Strings

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

##### Multiple F-Strings to print multiple strings or lines to the screen.

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

##### Format Floating-Point Decimals

#      f'{value:{width}.{precision}}'

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

