def greet_students(name, nChar):
    for i in range (nChar):
        print (name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)