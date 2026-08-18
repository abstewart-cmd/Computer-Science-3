# Get the birth year of user. Very important.
birth_year = int(input("Enter your birth year: "))

# Placeholder of the zodiac for now.
chinese_zodiac_sign = str("Empty")

# Start the first selection structure. If birth year < 1900, it will end the program.
if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900.")

# Though, if birth year is instead > 1900, then it selects their zodiac based on its divisibility by 12, and changes the variable's contents to the corresponding string.
else:
    if birth_year % 12 == 0:
        chinese_zodiac_sign = "Monkey (猴 / Hóu)"

    elif birth_year % 12 == 1:
        chinese_zodiac_sign = "Rooster (鸡 / Jī)"

    elif birth_year % 12 == 2:
        chinese_zodiac_sign = "Dog (狗 / Gǒu)"

    elif birth_year % 12 == 3:
        chinese_zodiac_sign = "Pig (猪 / Zhū)"

    elif birth_year % 12 == 4:
        chinese_zodiac_sign = "Rat (鼠 / Shǔ)"

    elif birth_year % 12 == 5:
        chinese_zodiac_sign = "Ox (牛 / Niú)"

    elif birth_year % 12 == 6:
        chinese_zodiac_sign = "Tiger (虎 / Hǔ)"

    elif birth_year % 12 == 7:
        chinese_zodiac_sign = "Rabbit (兔 / Tù)"

    elif birth_year % 12 == 8:
        chinese_zodiac_sign = "Dragon (龙 / Lóng)"

    elif birth_year % 12 == 9:
        chinese_zodiac_sign = "Snake (蛇 / Shé)"

    elif birth_year % 12 == 10:
        chinese_zodiac_sign = "Horse (马 / Mǎ)"
    
    elif birth_year % 12 == 11:
        chinese_zodiac_sign = "Goat (羊 / Yáng)"

    # Just incase somebody makes the most IMPOSSIBLE error ever, you know?
    else:
        print("There seems to have been an impossible error. Try again!")

# Finally, tell the user their zodiac sign.
print("Your Chinese Zodiac Sign is : ", chinese_zodiac_sign)