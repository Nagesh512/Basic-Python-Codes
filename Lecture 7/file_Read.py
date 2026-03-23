# Python can be used to perform operations on a file(read and Write)

# Python can access read write append data in a files


# Types of files
# Text Files = .txt, .doc, .log etc
# Binary Files = .mp4, .mov. .png, .jpeg etc

# OPEN, READ & CLOSE
# We have to open file before reading or writing

# f = open("file_name", "mode")

f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

