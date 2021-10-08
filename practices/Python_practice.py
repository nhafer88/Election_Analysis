#List
counties=["Arapahoe","Denver","Jefferson"]
#Dictionary
counties_dict={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
#List of Dictionaries
voting_data=[{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]

#Conditionals
if counties[1]=='Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print ("El Paso is not the list of counties.")

#Compound Membership and Logical operations  
if "Arapahoe" in counties or "El Paso" in counties:
    print ("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

#For Loop (new variable is county)
for county in counties:
    print (county)

#For Loop using range function
for i in range(len(counties)):
    print (counties [i])

#For Loop w/Dictionary-finding the keys
for county in counties_dict:
    print (county)
# Using keys method
for county in counties_dict.keys():
    print (county)

#For Loops w/Dictionary-finding the values
for voters in counties_dict.values():
    print(voters)
# Using dictionary_name[key]
for county in counties_dict:
    print(counties_dict[county])

# Using get() method
for county in counties_dict:
    print(counties_dict.get(county))

#For Loop for getting key-value pairs
for county, voters in counties_dict.items():
    print(county, voters)

#For Loop through a list of Dictionaries
#get each Dictionary
for county_dict in voting_data:
    print(county_dict)
#Use of range() function
for i in range(len(voting_data)):
    print(voting_data[i])
#retrieving values using nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#retrieving num of registered voters
for county_dict in voting_data:
    print(county_dict["registered_voters"])
#retrieving county names
for county_dict in voting_data:
    print(county_dict["county"])

#Difference using f-strings with concatenation
# w/o f
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
# w/ f--->added , seperator
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

# Import Dependencies (Datetime Module), print current time

#Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
#Print the present time.
print("The time right now is", now)

#Find all the attributes and methods using dir()
print(dir(str))
