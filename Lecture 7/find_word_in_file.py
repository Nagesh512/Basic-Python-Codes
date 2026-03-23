def check_for_word(word):
    with open("practice.txt", "r") as f:
        data = f.read()

        if (data.find(word) != -1):
            print("found")
        else:
            print("Not found")
    
check_for_word("learning")

def check_for_line(word):
    data = True
    line = 1
    with open("practice.txt", "r") as f:
        
        while data:
            data = f.readline()

            if (word in data):
                print(line)
                return  
            line+=1
    return-1

print(check_for_line("learninsdf"))
