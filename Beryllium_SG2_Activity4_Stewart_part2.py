def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0 : nChar])

name = input("Enter a Name")
greet_students(name, len(name))