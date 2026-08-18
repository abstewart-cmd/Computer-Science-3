def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0 : nChar])

name = input("Enter a Name")
greet_students(name, len(name))

# a. So, name[0:nChar] always uses the same nChar, meaning it doesn't change inside the loop.
# To change it, you can modify print(name[0 : nChar]) into print(name[0 : i]), but since range() starts at 0, this would print nothing.
# So just count backward from the name length.

# b. Now, the range should be modified from range(nChar) into range(nChar, 0, -1), based on sources.
# This apparantly means that it starts at nChar which is 6, stop before 0, and decreases it by 1 each time. So i becomes:

    #6
    #5
    #4
    #3
    #2
    #1

# And then name[0:i] takes the name characters until i, so for Joseph:

    #name[0:6] --> Joseph
    #name[0:5] --> Josep
    #name[0:4] --> Jose
    #name[0:3] --> Jos
    #name[0:2] --> Jo
    #name[0:1] --> J

# And of course. To make stuff look a little cleaner, we can add a ": " to the input prompt for a name.
# So, the code will turn into...