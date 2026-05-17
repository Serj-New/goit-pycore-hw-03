from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming = []
    
    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # День народження у цьому році
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо вже був — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Різниця в днях
        delta_days = (birthday_this_year - today).days
        
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year
            
            # Якщо субота (5) або неділя (6)
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            
            upcoming.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming

# Перевірка:
users = [
    {"name": "John Doe", "birthday": "1985.05.23"},
    {"name": "Jane Smith", "birthday": "1990.05.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)