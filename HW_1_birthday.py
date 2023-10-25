from datetime import datetime, timedelta
from collections import defaultdict

    # users - list of dictionaries, each with keys 'name' and 'birthday'
def get_birthdays_per_week(users):

    # get today's date
    today = datetime.today().date()

    # next week date
    next_week_start = today + timedelta(days=7)

    # dict for names
    b_day_by_day = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # date type conversion
        birthday_this_year = birthday.replace(year=today.year)
        
        # check if b-day passed
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # difference between the b-day and the current day
        delta_days = (birthday_this_year - today).days

        # determine b-day weekday
        birthday_weekday = birthday_this_year.strftime("%A")
        
        # transfer to weekday
        if today <= birthday_this_year <= next_week_start:
            if delta_days == 0:
                day_of_week = "Today"
            else:
                if birthday_weekday in ["Saturday", "Sunday"]:
                    day_of_week = "Monday"
                else:
                    day_of_week = birthday_weekday
            b_day_by_day[day_of_week].append(name)


    # result
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        if b_day_by_day [day]:
            print(f"{day}: {', '.join(b_day_by_day [day])}")


users = [
    {"name": "Colleague0", "birthday": datetime(1966, 10, 25)},
    {"name": "Colleague1", "birthday": datetime(1966, 10, 26)},
    {"name": "Colleague2", "birthday": datetime(1995, 10, 27)},
    {"name": "Colleague3", "birthday": datetime(1971, 10, 28)},
    {"name": "Colleague4", "birthday": datetime(1985, 10, 29)},
    {"name": "Colleague5", "birthday": datetime(1980, 10, 30)},
    {"name": "Colleague6", "birthday": datetime(1976, 10, 31)},
    {"name": "Colleague7", "birthday": datetime(1976, 11, 1)},
    {"name": "Colleague8", "birthday": datetime(1976, 11, 2)},
    {"name": "Colleague9", "birthday": datetime(1976, 11, 3)},
    {"name": "Colleague10", "birthday": datetime(1976, 11, 4)},
    {"name": "Colleague11", "birthday": datetime(1976, 11, 5)},
]

get_birthdays_per_week(users)

