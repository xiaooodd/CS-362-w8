# year=int(input("Please enter a year: "))
# if    year % 400 = = 0 or year % 4 = = 0 and year % 100 != 0:
#     print ("It's a leap year")
# else:
#     print("It's not a leap year")

def is_leap(x):
    if (x % 4) == 0:
        if (x % 100) == 0:
            if (x % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False