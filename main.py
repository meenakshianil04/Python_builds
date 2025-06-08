import datetime,bday_messages
today = datetime.date.today()
next_bday =datetime.date(2025,10,16)
days_away = next_bday- today
if (today == next_bday):
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')