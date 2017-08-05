a=int(input("Enter the year: "))
if (a%4)==0:
    if (a%100)==0:
        if(a%400)==0:
            print("%s is a leap year"%a)
        else:
            print("%s not a leap year"%a)
    else:
        print("%s is a leap year"%a)
else:
    print("%s is a leap year"%a)
                
