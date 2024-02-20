from datetime import datetime, timedelta

today = datetime.now()
tommorow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)

formed_today = today.strftime("%d-%m-%Y")
formed_tommorow = tommorow.strftime("%d-%m-%Y")
formed_yesterday = yesterday.strftime("%d-%m-%Y")

print("Yesterday:", formed_yesterday)
print("Today:", formed_today)
print("Tommorow:", formed_tommorow)