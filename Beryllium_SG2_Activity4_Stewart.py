def greet_students(name, nChar):
    for i in range(nChar):
       if i < len(name):
           print(name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)

# a. The output, if name = Joseph The Dreamer and nChar = 5, will be:
    # J
    # o
    # s
    # e
    # p
# Starts from index 0 and makes 5 characters. Because range(5) gives 0, 1, 2, 3, 4, so it will call name[0] to name[4]

# b. The output, if name = Joseph The Dreamer and nChar = 5, will be:
    #J
    #o
    #s
    #e
    #p
    #h
    
    #T
    #h
    #e
    
    #D
    #r
    #e
    #a
    #m
    #e
    #r

# Which is 0 to 17, the valid indexes. But range(20) produces until index 19. 
# This means the program prints the first 18 characters properly, but then stops at name[18] because there is no character there.
# And so, there will be an error. IndexError: string index out of range, since the program is trying to access characters out of the range of the string.

# c. Now, with sources online, It's possible to rewrite the loop like this...
    # for i in range(nChar):
    #   if i < len(name):
    #       print(name[i])

# Meaning that if name = Joseph The Dreamer and nChar = 20, it will print all 18 characters and stop, while no longer producing an IndexError.