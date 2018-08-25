import threading
import time
#build 4 thrads
# thread one gueses from 10**(len(pin)-1) going foward
status=0
def start(number):
    f=10**(int(len(str(number)))-1)
    return f
def thread1(pin):
    s=start(pin)
    for x in range(10**int(len(str(pin)))):
        global status
        if(status!=1):
            if (s!=int(pin)):
                s=s+1
            else:
                print "From thread 1 Your pin is \n"+str(s)
                status=1
                break;
        else:
            break;
# thread two gueses from (len(pin))*"9" going going backwards
def thread2(pin):
    b=int(len(str(pin)))*"9"
    n=int(b)
    for x in range (10**int(len(str(pin)))):
        global status
        if (status!=1):
            if (n!=int(pin)):
                n=n-1
            else:
                print "From thread2 Your pin is \n"+str(n)
                status=1
                break;
        else:
            break;
# thread three gueses from (10**(len(pin)-1))/2 going foward
# thread four gueses from (10**(len(pin)-1))/2 going backwards
def crack():
    number=raw_input("Enter the number of in your pin\n");
    pin=raw_input("Enter your pin\n")
    stime=time.time()
    #t0=thrading.Thread(target=timer,name='timer',args=(stime,))
    t1=threading.Thread(target=thread1,name='thread1',args=(pin,))
    t2=threading.Thread(target=thread2,name='thread2',args=(pin,))
    t1.start()
    t2.start()
crack()
