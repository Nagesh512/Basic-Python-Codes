f = open("Lecture 7/demo.txt", "w")

f.write("I want to learn Pyspark from Tomorrow")

f.close()

f = open("Lecture 7/demo.txt", "a")
f.write("\nThen I will move to Databricks")
f.close()

f = open("Lecture 7/demo.txt", "r")
data = f.read()
print(data)