# Dictionary 
# Dictionaries are used to store data values in key:value pairs
# “key” : value
# They are unordered(i.e. no indexing it is differentiate based on the keys),
# mutable(changeable) & don’t allow duplicate keys

Info = {
    "key" : "value",
    "name" : "Nagu",
    "Learning" : "coding",
    "age" : 23,
    "marks" : 98.3,
    "is_adult" : True
}
print(Info)
print(type(Info))
print(Info["name"])
print(Info["marks"])
Info["name"] = "Nagesh"
Info["surname"] = "Salunke"
print(Info["name"])
print(Info["surname"])


# We can store lists and tuple in an dictionary 
# We cannot use list and dictionary as keys / keys name should not as ....
# keys can be string, integer, floating value, or boolean


Info1 = {
    "name" : "Nagesh",
    "Subject" : ["Python", "Java" , "C"],
    "topics" : ("dictionary", "set"),
    8 : 12,
    12.44 : 144,

    
}
print(Info1["Subject"])

# We can create null dictionary

null_dict = {}
print(null_dict)
print(type(null_dict))