from datetime import datetime, timedelta

current_day = datetime.now()

five_day_before = current_day - timedelta(days = 5)

formed_date = five_day_before.strftime("%d-%m-%Y")

print(formed_date)