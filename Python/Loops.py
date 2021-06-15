#Loops
def main():
    x=0
    while(x<3):
        print(x)
        x=x+1                     #print normal 0,1,2

    for i in range(5,10):
        print(i)                  #print 5,6,7,8,9 (note 10 is exclude)

    week=["mon","tues","wed","thurs","fri","sat","sun"]
    for i in week:
        print(i)                  #iterate thorugh week and print values

    week=["mon","tues","wed","thurs","fri","sat","sun"]
    for i,d in enumerate(week):    #enumerate function gives index and values both
        print(i, d)        

    for i in range(5,10):
        if(i==7): break
        print(i)                  #o/p 5,6 breaks the loop when condition met

    for i in range(5,10):
        if (i%2==0): continue    
        print(i)                 #o/p where condition not met for continue 5,7,9 for 6, and 8 below code are skipped using continue

if __name__=="__main__":
    main()        