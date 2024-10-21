age = 17

if(age > 18):
    print("Can Vote and Apply for lisence")

else:
    print("Cant vote")

light = "red"
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("go")
elif(light == "Yellow"):
    print("Look")
else:
    print("traffic light is broken ")

# Indentation -- proper spacing 
# in python we dont use curly braces so we must give proper space/ indentation is must in python code
# otherwise code will not work

marks = int(input("Enter your marks then i will give you your grade"))

if(marks >= 90):
    print("A grade")
elif(90 > marks >= 80):
    print("B grade")
elif(80 > marks >= 70):
    print("C grade")
elif(70 > marks >= 60):
    print("D grade")
else:
    print("E grade")