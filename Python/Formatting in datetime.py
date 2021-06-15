#formatting in datetime
from datetime import datetime
#code not working
def main():
    current_timestamp = datetime.now()
    #formatting for date  :- %D day of month, %B =Month, %Y= Year, %A =weekday
    print(current_timestamp.strftime("the current year is : %Y"))
    #fromating for locale's :- %c =locale's date and time, %x =local date, %X= local time
    #formatting for time :- %I/%H 12/24hr, %H= Hour , %M= Minutes , %p =am/pm
    print("hi")
if __name__ == "__main__" :
    main()