birth_year = int(input("Enter your birth year: "))
chinese_zodiac_sign = str("")

if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900.")

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

    else:
        print("There seems to have been an impossible error. Try again!")

print("Your Chinese Zodiac Sign is : ", chinese_zodiac_sign)