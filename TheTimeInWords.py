h = 8
m = 40
names = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
         "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
if m == 0:
    print(names[h] + " o' clock")
elif m % 15 ==0:
    if m / 15 == 1:
        print("quarter past " + names[h])
    elif m / 15 == 2:
        print("half past "+names[h])
    elif m / 15 == 3:
        print("quarter to " + names[(h+1) % 12])
else:
    if m > 30:
        f = 60 - m
        if f > 20:
            print("twenty " + names[f % 20] + " minutes to " + names[(h+1) % 12])
        elif f == 20:
            print("twenty minutes to " + names[(h+1) % 12])
        else:
            if f == 1:
                print("one minute to " + names[(h + 1) % 12])
            else:
                print(names[f] + " minutes to " + names[(h + 1) % 12])
    else:
        if m > 20:
            print("twenty " + names[m % 20] + " minutes past " + names[h])
        elif m == 20:
            print("twenty minutes past " + names[(h+1) % 12])
        else:
            if m == 1:
                print("one minute past " + names[h])
            else:
                print(names[m] + " minutes past " + names[h])