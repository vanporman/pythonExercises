
#from datetime import date
from datetime import datetime, date
today = datetime.utcnow()
#today = date.today()
today2 = datetime.date(today)
today3 = datetime.date(today)

birthdate = "1987-05-05"
mybirthday = datetime.strptime(birthdate, "%Y-%m-%d")
#print (mybirthday)
mybirthday2 = datetime.date(mybirthday)

def get_age(birth_date, current_date=today3):
    #today3 = datetime.utcnow()
    #today4 = datetime.date(today3)
    #timenow = current_date.strftime("%Y-%m-%d")
    print (current_date)
    print (birth_date)

    age = (current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day)))
    print (age)
    return age
    #print (current_date.year - mybirthday.year)
    #print (current_date.month, current_date.day)
    #print (mybirthday.month, mybirthday.day)

get_age(mybirthday2, today2)
get_age(mybirthday2)

