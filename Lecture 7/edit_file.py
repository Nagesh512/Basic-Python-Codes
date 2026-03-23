def replace_in_file(new):
    with open("practice.txt","r") as f :
        data = f.read()

    new_data = data.replace("Java", new)
    print(new_data)

    with open("practice.txt", "w") as f:
        f.write(new_data)

replace_in_file("Python")