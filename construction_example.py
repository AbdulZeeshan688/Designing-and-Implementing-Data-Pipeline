''' Use class level attributes(root of the class ) only for the values that are same for every object
example :
-Number of weeels in a car 
- pi contant 
- configuration shared by all instances 
- version number '''

class car :
    wheels = 4 # same for all cars as a default

'''
these attributes live in a class , not the object 
use constructor (__init__) for instacne-specific data. they are unique object 
examples ;
- car colour 
- max speed
- CURRENT CAR
- registration number
'''

class car :
    weels = 4 # shared by default by all cars 

    def __init__(self, color, max_speed ):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

'''
Every time you create a new object contructor which means the init runs and guves the specific object it own attributes.
why not put object-specific atttributes in the roots ? because attributes in the roots are shared unless overwritten .
for example :
'''

class person :
    hobbies = [] # shared list 

p1 = person()
p2 = person()

p1.hobbies.append("football ")
p1.hobbies.append("Reading")
p2.hobbies.append("Making music ")

#print(p1.hobbies) # ['Reading']
print(p2.hobbies) # ['Reading', 'Traveling']

'''
If the list was inside __init__, each person would have their own list.
'''

class student :
    def __init__(self, name):
        self.name = name
        self.hobbies = []  # unique to each student

s1 = student("Alice")
s2 = student("Bob")

s1.hobbies.append("Drawing")
s2.hobbies.append("Playing guitar")

print(s1.hobbies)  # ['Drawing']
print(s2.hobbies)  # ['Playing guitar']
