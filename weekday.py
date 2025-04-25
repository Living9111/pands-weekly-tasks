
import datetime

weekno = datetime.datetime.today().weekday()

if weekno < 5:
    print ('Yes, unfortunately today is a weekday')
else:  # 5 Sat, 6 Sun
    print ('It is the weekend, yay!')


