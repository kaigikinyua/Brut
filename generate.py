class Generate():
    def details(self):
        values=[];
        print ("Enter .,., to quit")
        while(1):
            ans=raw_input()
            if(ans==".,.,"):
                break;
            else:
                values+=[ans]
        return values
