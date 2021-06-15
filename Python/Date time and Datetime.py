from datetime import date                  #datetime is a standard python linrary and we are importing date,time and datetime classes
from datetime import time
from datetime import datetime


def main():
    todays_date=date.today()                                        #with date object today method is called.
    print(todays_date)
    print("today days component",todays_date.day,todays_date.month,todays_date.year) #these are not function

    print("todays weekday in number",todays_date.weekday())              #this is a function
    weekday=['mon','tue','wed','thurs','fri','sat','sun']              
    print("todays weekday is ",weekday[todays_date.weekday()])            #index is getting from function



    print("current datetime",datetime.now())                                  #now function is used
    print("extarcting time from datetime",datetime.time(datetime.now()))         #to extarct time time() is used
    print("extarcting date from datetime",datetime.now().day,datetime.now().month,datetime.now().year)       #extracting components.

main()    