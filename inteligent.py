#inteligent guessing
from generate import *
class Inteli():
    def __init__(self):
        fp=open("pass.txt","r")
        g=fp.readlines()
        if(len(g)<1):
            fp.close();fp=open("pass.txt","w")
            print "No inteligent guesses"
            g=Generate()
            gen=g.details()
            for value in gen:
                fp.write(value+"\n")
            fp.close()
        else:
            print "You have some guesses"
            fp.close()
i=Inteli()
