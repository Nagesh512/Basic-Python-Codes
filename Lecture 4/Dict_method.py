Student = {
    "name" : "Nagu",
    "Subjects" : {
        "phy" : 60,
        "chem" : 71,
        "math" : 98
    }
}

print(Student.keys())  # gives list of keys
print(len(Student))   # Total number of keys
print(list(Student.keys()))   # save keys in the list
print(Student.values())     # gives all the values store in a dictionary
print(Student.items())      # Gives all the key and value pair in the form of tuple(key,value)

pairs = list(Student.items())  # saves in the form of list 
print(pairs[0])     #access it as the list members

print(Student["name"])
print(Student.get("name"))

# print(Student["name2"])       it will give the error as we dont create any key of name name2
print(Student.get("name2"))       #--> it will not give any error it will simply shows None As we not assign any key name as name2 

Student.update({"city" : "Nanded"})   #In this we can pass {key : value} or we can insert any another dictionary 
print(Student)

dict = {"Cur_City": "Pune","age" : 23, "name" : "Nagesh"}
Student.update(dict)
print(Student)