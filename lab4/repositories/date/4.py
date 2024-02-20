from datetime import datetime, timedelta

date_1 = datetime.now()
date_2 = date_1 + timedelta(days = 1)

date1 = date_1.strftime("%Y-%m-%d %H:%M:%S")
date2 = date_2.strftime("%Y-%m-%d %H:%M:%S")

time_difference = date2 - date1

result = time_difference.total_seconds()

print(result)