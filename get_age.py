
#from datetime import date
from datetime import datetime, date
#today = datetime.utcnow()

today = date.today()

def get_age(birth_date, current_date=None):
    #utcnow = datetime.utcnow()
    #timenow = current_date.strftime("%Y-%m-%d")
    print (current_date)

    #mybirthday = date.strptime(birth_date, "%Y-%m-%d")#
    mybirthday = datetime.strptime(birth_date, "%Y-%m-%d") #<---siin on kala!!!!!!
    print (mybirthday)

    age = (current_date.year - mybirthday.year - ((current_date.month, current_date.day) < (mybirthday.month, mybirthday.day)))
    print (age)
    #print (current_date.year - mybirthday.year)
    #print (current_date.month, current_date.day)
    #print (mybirthday.month, mybirthday.day)
    return age

get_age("1987-05-05", today)
get_age("1983-07-09", today)
