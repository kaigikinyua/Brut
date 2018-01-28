def values_(number):
    n=str(number)
    f=int(number)*"0"
    return f
def crack():
    number=raw_input("Enter the number of in your pin\n");
    pin=raw_input("Enter your pin\n")
    p_size=(str(pin))
    n=int(values_(number))
    s=len(pin)
    for x in range(10**int(s)):
        if(int(pin)!=n):
            print n
            n=n+1
        else:
            print "Here is your pin"
            print n
            break;
crack()
