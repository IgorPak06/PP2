from datetime import datetime 

current_date = datetime.now()

datetime_check = current_date.replace(microsecond = 0)

print(datetime_check)